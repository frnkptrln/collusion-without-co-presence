# from peer-pressure-without-peers@9b048f1 (prior work); changed 2026-10 for this repository — every change is marked NEW 2026-10
"""Freeze the instrument: hash the bound pre-registration and the instrument files into MANIFEST.sha256.json.

  python3 freeze.py --preregistration ../PREREGISTRATION.md --note "bound 2026-10-21; hand-off A"

Refuses to run if a main-phase run directory already contains a started episode. A re-freeze after a logged deviation
takes --version v2, v3, … and writes MANIFEST.sha256.v2.json beside the first manifest (never over it).
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
# NEW 2026-10: the files of this repository's instrument (sweep_e4.py and run_open_r3.py are not part of it; gate.py is)
INSTRUMENT = ("fixtures_r3.py", "run_r3.py", "analyze_r3.py", "workspace_server.py", "concern_server.py",
              "schema.py", "stats.py", "report.py", "gate.py")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preregistration", default=str(HERE.parent / "PREREGISTRATION.md"))   # NEW 2026-10 (was --amendment)
    ap.add_argument("--note", default="")
    ap.add_argument("--version", default="", help="suffix for a re-freeze after a logged deviation, e.g. v2")
    a = ap.parse_args()
    if "[BIND]" in Path(a.preregistration).read_text(encoding="utf-8"):   # NEW 2026-10: an unbound pre-registration is not frozen
        raise SystemExit("refusing to freeze: PREREGISTRATION.md still has [BIND] placeholders")
    for plan in (HERE / "runs").glob("*/plan.json"):   # NEW 2026-10: any main-phase run, whatever its directory name
        p = json.loads(plan.read_text(encoding="utf-8"))
        run = plan.parent
        if p.get("phase") == "main" and any((ep / "started.json").exists() for ep in run.iterdir() if ep.is_dir()):
            raise SystemExit(f"refusing to freeze: main-phase episodes already started in {run}")
    manifest = {"frozen_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "note": a.note,
                "preregistration": {str(a.preregistration): sha(a.preregistration)},
                "instrument": {f: sha(HERE / f) for f in INSTRUMENT}}
    out = HERE / (f"MANIFEST.sha256.{a.version}.json" if a.version else "MANIFEST.sha256.json")
    if out.exists():
        raise SystemExit(f"{out.name} exists; a re-freeze needs --version")
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
