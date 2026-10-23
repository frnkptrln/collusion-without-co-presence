# from peer-pressure-without-peers@9b048f1 (prior work); changed 2026-10 for this repository — every change is marked NEW 2026-10
"""Freeze the instrument: hash the bound pre-registration, the instrument, the runbook and the analysis into MANIFEST.sha256.json.

  python3 freeze.py --preregistration ../PREREGISTRATION.md --note "bound 2026-10-21; hand-off A"

NEW 2026-10 (V7, 21 Oct): refuses while the pre-registration still carries a `[BIND]` or a `[FRANK]` placeholder; the manifest
keys are repository-relative paths (`PREREGISTRATION.md`, `instrument/fixtures_r3.py`, `analysis/report.py`, …), so a
frozen tree verifies at any path; it covers the instrument files, the runbook (`instrument/sprint_autorun.py`,
`instrument/quota.py`) and every `analysis/*.py`. `verify_manifest()` is what `sprint_autorun.py --phase check` runs.

Refuses to run if a main-phase run directory already contains a started episode. A re-freeze after a logged deviation
takes --version v2, v3, … and writes MANIFEST.sha256.v2.json beside the first manifest (never over it).
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# NEW 2026-10: the files of this repository's instrument (sweep_e4.py and run_open_r3.py are not part of it; gate.py is)
INSTRUMENT = ("fixtures_r3.py", "run_r3.py", "analyze_r3.py", "workspace_server.py", "concern_server.py",
              "schema.py", "stats.py", "report.py", "gate.py")
RUNBOOK = ("sprint_autorun.py", "quota.py")   # NEW 2026-10 (V7): the runbook carries the model id and the batch structure
PLACEHOLDERS = ("[BIND]", "[FRANK]")          # NEW 2026-10 (V7): both block the freeze


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def frozen_files(preregistration):
    """{repository-relative path: absolute path} of everything the manifest covers."""
    files = {str(Path(preregistration).resolve().relative_to(REPO)): Path(preregistration).resolve()}
    for f in INSTRUMENT + RUNBOOK:
        files[f"instrument/{f}"] = HERE / f
    for p in sorted((REPO / "analysis").glob("*.py")):
        files[f"analysis/{p.name}"] = p
    return files


def verify_manifest(path):
    """NEW 2026-10 (V7): the files of a manifest against the repository they sit in. Returns (manifest, mismatches)."""
    m = json.loads(Path(path).read_text(encoding="utf-8"))
    bad = []
    for rel, h in m["files"].items():
        p = REPO / rel
        if not p.exists() or sha(p) != h:
            bad.append(rel)
    return m, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preregistration", default=str(REPO / "PREREGISTRATION.md"))   # NEW 2026-10 (was --amendment)
    ap.add_argument("--note", default="")
    ap.add_argument("--version", default="", help="suffix for a re-freeze after a logged deviation, e.g. v2")
    a = ap.parse_args()
    text = Path(a.preregistration).read_text(encoding="utf-8")
    open_items = {ph: text.count(ph) for ph in PLACEHOLDERS if ph in text}
    if open_items:   # NEW 2026-10: an unbound pre-registration, or one with the author's decisions open, is not frozen
        raise SystemExit("refusing to freeze: PREREGISTRATION.md still has placeholders " + ", ".join(f"{k} ×{v}" for k, v in open_items.items()))
    for plan in (HERE / "runs").glob("*/plan.json"):   # NEW 2026-10: any main-phase run, whatever its directory name
        p = json.loads(plan.read_text(encoding="utf-8"))
        run = plan.parent
        if p.get("phase") == "main" and any((ep / "started.json").exists() for ep in run.iterdir() if ep.is_dir()):
            raise SystemExit(f"refusing to freeze: main-phase episodes already started in {run}")
    files = frozen_files(a.preregistration)
    manifest = {"frozen_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "note": a.note,
                "groups": {"preregistration": [next(iter(files))], "instrument": [f"instrument/{f}" for f in INSTRUMENT],
                           "runbook": [f"instrument/{f}" for f in RUNBOOK], "analysis": [k for k in files if k.startswith("analysis/")]},
                "files": {rel: sha(p) for rel, p in files.items()}}
    out = HERE / (f"MANIFEST.sha256.{a.version}.json" if a.version else "MANIFEST.sha256.json")
    if out.exists():
        raise SystemExit(f"{out.name} exists; a re-freeze needs --version")
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
