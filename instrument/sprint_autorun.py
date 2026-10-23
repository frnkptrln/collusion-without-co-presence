#!/usr/bin/env python3
# from peer-pressure-without-peers@9b048f1 (prior work); rewritten 2026-10 for the sprint design — the September batches
# (friday / saturday / d4 / e4) are gone, the helpers (quota, streams, waves, logging, preflight) are the September ones.
"""Autonomous runner for the sprint batches — the runbook, executed by a script (outside the frozen instrument).

  python3 sprint_autorun.py --phase gate                       # Thursday: replacement chains 2 per arm (40) + positive control (4),
                                                               #   then gate.py — the verdict is logged, the fallback is printed, never executed
  python3 sprint_autorun.py --phase main                       # Friday: replacement chains 16 per arm (320) + positive control (16)
  python3 sprint_autorun.py --phase analysis                   # re-analyse and redraw every run directory; no model call
  python3 sprint_autorun.py --phase check                      # before a start: doctor, freeze verification, tests, quota; no model call
  … --backend rehearsal [--rehearsal-policy chain_payload]     # the same mechanics without a model (tests, dry runs)
  … --phase gate --handoff B                                   # the re-gate of §4.6 after a dead-channel gate (DEVIATIONS entry first):
                                                               #   a separate run gate-B on fresh pilot chains (seed base 920000), the
                                                               #   gate's positive control reused, verdict GATE_VERDICT_B.json
  … --phase main --handoff B                                   # the main design with wording B after that

What it does per batch, exactly as PREREGISTRATION.md §4 and §9: quota check (no batch above 80 % seven-day / 85 % five-hour;
if above, it waits for the window to reset — the reading comes from the last live episode's rate_limit_event) → prepare
(skipped when the directory already holds a plan: the script is restartable and never reruns an episode) → four
streams → wait → continuation rounds for streams that stopped on a transport/infrastructure error (finished and
interrupted episodes are skipped by the runner itself) → analyze → figures. Chain designs run wave-wise (one generation
per wave across all chains and arms). There is no outcome-dependent stopping: every planned generation of every chain
is run (§4, "no stopping rule"). Everything is appended to runs/AUTORUN_LOG.md.

Nothing here changes a plan, a prompt or an outcome; it only issues the runbook's commands in the runbook's order.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable
LOG_DIR = HERE / "logs"          # set per run root in main(): <runs>/_logs
HAIKU = "claude-haiku-4-5-20251001"
DESIGNS_WITH_REPORT = ("a", "b", "tier", "tier-full", "pc", "replacement")


# ---------------------------------------------------------------------------- batches

GATE_DIR = {"A": "gate", "B": "gate-B"}                       # NEW 2026-10 (V6): the re-gate with wording B is its own run
GATE_VERDICT = {"A": "GATE_VERDICT.json", "B": "GATE_VERDICT_B.json"}


def batches(phase, runs, handoff):
    """The runbook as data. kind: 'stream' (one wave), 'waves' (chain designs: one generation per wave). With --handoff B
    the gate phase prepares gate-B (fresh pilot chains, seed base 920000); the positive control is the gate's (pc-gate,
    resumed if it exists, never rerun)."""
    gate = [
        dict(name=f"gate — replacement chains, 2 per arm (pilot seeds, never pooled; hand-off wording {handoff})", out=f"{runs}/{GATE_DIR[handoff]}",
             kind="waves", design="replacement", generations=5,
             prepare=["run_r3.py", "prepare", "--experiment", "E3", "--phase", "gate", "--design", "replacement",
                      "--handoff", handoff, "--model", HAIKU]),
        dict(name="gate — positive control, 4 episodes", out=f"{runs}/pc-gate", kind="stream", design="pc",
             prepare=["run_r3.py", "prepare", "--experiment", "E1", "--phase", "gate", "--design", "pc", "--model", HAIKU]),
    ]
    main = [
        dict(name="main — replacement chains, 16 per arm", out=f"{runs}/main", kind="waves", design="replacement", generations=5,
             prepare=["run_r3.py", "prepare", "--experiment", "E3", "--phase", "main", "--design", "replacement",
                      "--handoff", handoff, "--model", HAIKU]),
        dict(name="main — positive control, 16 episodes", out=f"{runs}/pc-main", kind="stream", design="pc",
             prepare=["run_r3.py", "prepare", "--experiment", "E1", "--phase", "main", "--design", "pc", "--model", HAIKU]),
    ]
    return {"gate": gate, "main": main, "analysis": [], "check": []}[phase]


# ---------------------------------------------------------------------------- helpers

class Log:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def __call__(self, msg):
        line = f"- {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())} — {msg}"
        print(line, flush=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def quota_reading(runs):
    """Last rate_limit_event under runs/ (the same source as quota.py). Returns (five_hour, seven_day, resets) or None.
    NEW 2026-10 (V9): a relative `runs` is resolved against the instrument directory, not the working directory."""
    runs = Path(runs) if os.path.isabs(str(runs)) else HERE / str(runs)
    files = sorted(glob.glob(os.path.join(str(runs), "*", "*", "stdout.jsonl")), key=os.path.getmtime)
    last = None
    for f in files[-5:]:
        try:
            with open(f, encoding="utf-8") as fh:
                for line in fh:
                    if '"rate_limit_event"' in line:
                        try:
                            last = json.loads(line)
                        except json.JSONDecodeError:
                            pass
        except OSError:
            pass
    if not last:
        return None
    info = last["rate_limit_info"]["unifiedWindows"]
    return {"five_hour": info["five_hour"]["utilization"], "seven_day": info["seven_day"]["utilization"],
            "resets": {w: info[w]["resetsAt"] for w in ("five_hour", "seven_day")}}


def wait_for_quota(runs, log, backend, max_wait_h):
    """With no reading at all (first live batch of a fresh tree) the batch starts and produces one."""
    if backend != "claude":
        return True
    deadline = time.time() + max_wait_h * 3600
    while True:
        q = quota_reading(runs)
        if q is None:
            log("quota: no rate_limit_event under runs/ yet — starting; the first episode produces a reading")
            return True
        ok = q["seven_day"] <= 0.80 and q["five_hour"] <= 0.85
        log(f"quota: five_hour {q['five_hour']:.0%}, seven_day {q['seven_day']:.0%} → {'allowed' if ok else 'NOT allowed'}")
        if ok:
            return True
        over = "seven_day" if q["seven_day"] > 0.80 else "five_hour"
        until = q["resets"][over] + 120
        if until > deadline:
            log(f"quota: {over} window resets at {time.strftime('%H:%M UTC', time.gmtime(until))}, beyond the wait limit — stopping here")
            return False
        log(f"quota: waiting for the {over} window to reset at {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(until))}")
        time.sleep(max(60, until - time.time()))


def run_cmd(args, log, cwd=HERE):
    r = subprocess.run([PY] + args, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        log(f"command failed ({r.returncode}): {' '.join(args)} — {r.stderr.strip()[-400:]}")
    return r


def unfinished(out, only=None):
    plan = json.loads((out / "plan.json").read_text(encoding="utf-8"))
    cells = plan["episodes"]
    if only:
        k, v = only.split("=", 1)
        cells = [c for c in cells if str(c.get(k)) == v]
    todo = [c["episode_id"] for c in cells if not (out / c["episode_id"] / "result.json").exists()]
    interrupted = [e for e in todo if (out / e / "started.json").exists()]
    return todo, interrupted


def run_streams(out, backend, streams, log, policy, only=None, rounds=3, timeout=420):
    """Four streams, wait, then continuation rounds while runnable episodes remain (the runner skips finished and
    interrupted episodes; deferred generations wait for their predecessors, which the caller handles via waves)."""
    for rnd in range(1, rounds + 1):
        todo, interrupted = unfinished(out, only)
        runnable = [e for e in todo if e not in interrupted]
        if not runnable:
            break
        log(f"{out.name}{' ' + only if only else ''}: round {rnd}, {len(runnable)} episode(s) to run, {len(interrupted)} interrupted (never rerun)")
        procs = []
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        for k in range(1, streams + 1):
            args = [PY, "run_r3.py", "run", "--out", str(out), "--backend", backend, "--limit", "999",
                    "--stream", f"{k}/{streams}", "--timeout", str(timeout)]
            if only:
                args += ["--only", only]
            if backend == "rehearsal":
                args += ["--policy", policy]
            lf = open(LOG_DIR / f"{out.name}-{(only or 'all').replace('=', '')}-r{rnd}-s{k}.log", "a", encoding="utf-8")
            procs.append((subprocess.Popen(args, cwd=HERE, stdout=lf, stderr=subprocess.STDOUT), lf))
        for p, lf in procs:
            p.wait()
            lf.close()
        todo, interrupted = unfinished(out, only)
        if not [e for e in todo if e not in interrupted]:
            break
    todo, interrupted = unfinished(out, only)
    log(f"{out.name}{' ' + only if only else ''}: done — {len(todo)} unfinished ({len(interrupted)} interrupted)")
    return todo, interrupted


def analyze(out, design, log):
    args = ["analyze_r3.py", str(out)] + (["--design", design] if design else [])
    r = run_cmd(args, log)
    if r.returncode == 0:
        log(f"{out.name}: analysed → {out / 'results.md'}")
    fig = run_cmd([str(HERE.parent / "analysis" / "figures.py"), str(out)], log)
    if fig.returncode == 0 and fig.stdout.strip():
        made = json.loads(fig.stdout.strip().splitlines()[-1]).get("figures", [])
        if made:
            log(f"{out.name}: figures {', '.join(Path(m).name for m in made)}")


def prepare(b, out, log):
    if (out / "plan.json").exists():
        log(f"{b['name']}: {out} already prepared — resuming, no episode is rerun")
        return True
    r = run_cmd(b["prepare"] + ["--out", str(out)], log)
    if r.returncode != 0:
        return False
    tail = [l.strip() for l in r.stdout.strip().splitlines() if "plan_hash" in l or "episodes" in l]
    log(f"{b['name']}: prepared {out} ({'; '.join(tail)[:160]})")
    return True


# ---------------------------------------------------------------------------- batch kinds

def run_batch(b, a, log):
    out = HERE / b["out"]
    if not wait_for_quota(a.runs, log, a.backend, a.max_wait_h):
        return False
    if not prepare(b, out, log):
        return False
    if b["kind"] == "stream":
        run_streams(out, a.backend, a.streams, log, a.rehearsal_policy)
        analyze(out, b["design"], log)
        return True
    if b["kind"] == "waves":
        for g in range(1, b["generations"] + 1):
            run_streams(out, a.backend, a.streams, log, a.rehearsal_policy, only=f"generation={g}")
        analyze(out, b["design"], log)
        return True
    log(f"unknown batch kind {b['kind']}")
    return False


def gate_verdict(a, log):
    """After the gate batches: gate.py over the chain gate (gate, or gate-B for the re-gate) and the positive control. The
    verdict is logged with its numbers; the fallback it names is a decision for Frank and a DEVIATIONS entry, never an
    automatic switch; a pass with invalid episodes under criterion (i) names the DEVIATIONS entry it needs."""
    runs = HERE / a.runs
    r = subprocess.run([PY, "gate.py", str(runs / GATE_DIR[a.handoff]), "--pc", str(runs / "pc-gate")], cwd=HERE, capture_output=True, text=True)
    verdict = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"decision": "ERROR", "reasons": [r.stderr[-300:]]}
    (runs / GATE_VERDICT[a.handoff]).write_text(json.dumps(verdict, indent=2) + "\n", encoding="utf-8")
    log(f"gate ({GATE_DIR[a.handoff]}): **{verdict.get('decision')}** — " + "; ".join(verdict.get("reasons", [])))
    if verdict.get("deviation_required"):
        log(f"gate: proceeds under criterion (i) with invalid episodes counted invalid — a DEVIATIONS entry is required before the main run: {verdict['deviation_required']}")
    if verdict.get("fallback"):
        log(f"gate: fallback (not executed; needs a DEVIATIONS entry and Frank's decision): {verdict['fallback']}")
    return verdict


def analysis_only(a, log):
    for plan in sorted(glob.glob(os.path.join(HERE, a.runs, "*", "plan.json"))):
        out = Path(plan).parent
        p = json.loads(Path(plan).read_text(encoding="utf-8"))
        design = p.get("design")
        if design in DESIGNS_WITH_REPORT:
            analyze(out, design, log)
        elif p.get("experiment") in ("E2", "E3"):
            analyze(out, None, log)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["gate", "main", "analysis", "check"], required=True)
    ap.add_argument("--backend", choices=["claude", "rehearsal"], default="claude")
    ap.add_argument("--rehearsal-policy", default="chain_payload")
    ap.add_argument("--handoff", choices=["A", "B"], default="A", help="the hand-off wording in force (B only after a DEVIATIONS entry)")
    ap.add_argument("--streams", type=int, default=4)
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--max-wait-h", type=float, default=6.0, help="how long to wait for a quota window to reset")
    ap.add_argument("--log", default=None)
    a = ap.parse_args()
    global LOG_DIR
    LOG_DIR = HERE / a.runs / "_logs"
    log = Log(a.log or (HERE / a.runs / "AUTORUN_LOG.md"))
    log(f"### autorun --phase {a.phase} --backend {a.backend} --handoff {a.handoff} (streams {a.streams}); source hash {source_hash()[:12]}…")
    if a.phase == "analysis":
        analysis_only(a, log)
        log("analysis phase done")
        return
    if a.phase == "check":
        ok = preflight(a, log)
        gates_present = any((HERE / a.runs / d / "plan.json").exists() for d in ("gate", "gate-B"))
        log(("check: READY — start with --phase main" if gates_present else "check: READY — start with --phase gate") if ok else "check: NOT READY — see above")
        sys.exit(0 if ok else 1)
    for b in batches(a.phase, a.runs, a.handoff):
        log(f"## {b['name']}")
        ok = run_batch(b, a, log)
        if not ok:
            log(f"{b['name']}: stopped — see above; the remaining batches are not started")
            sys.exit(1)
    if a.phase == "gate":
        gate_verdict(a, log)
    log(f"phase {a.phase} done")


def newest_manifest():
    base = HERE / "MANIFEST.sha256.json"
    versions = sorted(HERE.glob("MANIFEST.sha256.v*.json"), key=lambda p: int(p.name.split(".v")[1].split(".")[0]))
    return versions[-1] if versions else (base if base.exists() else None)


def preflight(a, log):
    """Doctor, freeze verification against the newest manifest, tests, quota reading, existing run directories."""
    ok = True
    r = run_cmd(["run_r3.py", "doctor"], log)
    if r.returncode == 0:
        d = json.loads(r.stdout)
        log(f"doctor: claude_installed={d.get('claude_installed')} version={d.get('claude_version')} project_context_env_present={d.get('project_context_env_present')} "
            f"(scrubbed per episode) mcp_task={len(d.get('mcp_task_tools', []))} tools, mcp_concern={d.get('mcp_concern_tools')}")
        ok &= bool(d.get("claude_installed")) or a.backend == "rehearsal"
    else:
        ok = False
    manifest = newest_manifest()
    if manifest:
        sys.path.insert(0, str(HERE))
        from freeze import verify_manifest   # NEW 2026-10 (V7): repository-relative keys, verified wherever the tree sits
        m, bad = verify_manifest(manifest)
        log(f"freeze {manifest.name} ({m.get('frozen_at_utc')}): {len(m['files'])} files, " + ("all hashes match" if not bad else f"MISMATCH in {bad}"))
        ok &= not bad
    else:
        log("freeze: no MANIFEST.sha256.json — the instrument is not bound; a live batch needs the freeze first")
        ok &= a.backend == "rehearsal"
    r = subprocess.run([PY, "-m", "unittest", "discover", "-s", "tests"], cwd=HERE, capture_output=True, text=True)
    last = (r.stderr.strip().splitlines() or ["?"])[-1]
    log(f"tests: {last}")
    ok &= r.returncode == 0
    q = quota_reading(a.runs)
    log(f"quota: five_hour {q['five_hour']:.0%}, seven_day {q['seven_day']:.0%}" if q else "quota: no reading yet (first live episode produces one)")
    ok &= check_run_directories(HERE / a.runs, log)
    return bool(ok)


SPRINT_RUN_DIRS = ("gate", "gate-B", "pc-gate", "main", "pc-main")


def check_run_directories(root, log):
    """NEW 2026-10 (N13): run directories that already exist under the runs root. A sprint directory (gate, gate-B, pc-gate,
    main, pc-main) holding rehearsal episodes, or any main-phase directory, means NOT READY: the live batch would refuse to
    mix backends or would find its directory taken. Gate directories with live episodes are what a check before
    --phase main expects; the check then says it is ready for the main phase only. Returns ok."""
    root = Path(root)
    ok = True
    existing = sorted(p.parent.name for p in root.glob("*/plan.json")) if root.exists() else []
    log(f"run directories present: {existing}")
    sprint_dirs = [d for d in existing if d in SPRINT_RUN_DIRS]
    backends = {d: (json.loads((root / d / "backend.json").read_text(encoding="utf-8")).get("backend") if (root / d / "backend.json").exists() else None)
                for d in sprint_dirs}
    rehearsed = [d for d, b in backends.items() if b != "claude_code"]
    if rehearsed:
        log(f"NOT READY: {rehearsed} under {root} hold rehearsal episodes (or none) — a live batch cannot use them; move or delete them, or use another --runs root")
        ok = False
    if any(d in ("main", "pc-main") for d in sprint_dirs):
        log(f"NOT READY: a main-phase directory already exists under {root} — the main design is run once; nothing is rerun")
        ok = False
    gates = [d for d in sprint_dirs if d in ("gate", "gate-B", "pc-gate")]
    if ok and gates:
        latest = next((p for p in (root / "GATE_VERDICT_B.json", root / "GATE_VERDICT.json") if p.exists()), None)   # the re-gate's verdict, if any, is the latest
        if latest is None:
            log(f"NOT READY for --phase main: gate directories {gates} present but no verdict file — finish --phase gate (gate.py writes the verdict)")
            ok = False
        else:
            v = json.loads(latest.read_text(encoding="utf-8"))
            if v.get("decision") == "PASS":
                log(f"gate directories {gates} with live episodes, {latest.name}: PASS"
                    + (f" with a DEVIATIONS entry required first ({v['deviation_required']})" if v.get("deviation_required") else "")
                    + " — ready for --phase main only")
            elif latest.name == "GATE_VERDICT_B.json":
                log(f"NOT READY for --phase main: {latest.name} says {v.get('decision')} — the re-gate failed as well; the main run does not start; "
                    "the author decides what follows and records it as a DEVIATIONS entry (§4.6)")
                ok = False
            else:
                log(f"NOT READY for --phase main: {latest.name} says {v.get('decision')} — the pre-registered next step is the re-gate "
                    "(--phase gate --handoff B, after a DEVIATIONS entry) or a stop (§4.6)")
                ok = False
    return ok


def source_hash():
    sys.path.insert(0, str(HERE))
    import run_r3
    return run_r3.source_hash()


if __name__ == "__main__":
    main()
