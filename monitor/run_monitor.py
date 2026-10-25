#!/usr/bin/env python3
# Claude, 23 October 2026 — monitor study (new sprint work). Calls the auditor model through Claude Code headless on
# the same allowlisted environment as the subject sessions (imported from the frozen instrument, not changed).
"""Run the auditor over a states file.

  python3 monitor/run_monitor.py monitor/states/main/states.jsonl --model claude-haiku-4-5-20251001 \
      --prompt monitor/prompts/auditor_v1.md --out monitor/runs/main/haiku --views job,chain,plus
  python3 monitor/run_monitor.py ... --dry-run          # writes the exact commands and payloads, calls nothing
  python3 monitor/run_monitor.py ... --only-positives    # only states whose own job is READ or LEAK
  python3 monitor/run_monitor.py ... --limit 5

One call per state, no tools, no MCP servers, one turn. Every call is recorded in <out>/calls.jsonl: the state id, the
sha256 of the payload sent, the model requested and every model id the stream returned, the raw final text, the
parsed verdict (or the parse error), cost, elapsed time, exit code, and the diagnostics the CLI reports
(has_project_context, has_user_email). Re-running skips states already recorded, so a run can be resumed.
No episode of the subject instrument is touched; this script never writes under instrument/.
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "instrument"))
import run_r3  # noqa: E402  (frozen: subject_environment, parse_diag; imported, not changed)


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_system_prompt(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.search(r"<!-- SYSTEM -->\n(.*?)\n<!-- /SYSTEM -->", text, flags=re.S)
    if not m:
        raise ValueError(f"no SYSTEM block in {path}")
    return m.group(1).strip() + "\n"


def command(exe, model, system, effort):
    return [exe, "--restricted", "-p", "--tools", "", "--strict-mcp-config",
            "--permission-mode", "dontAsk", "--setting-sources", "",
            "--system-prompt", system, "--no-session-persistence",
            "--model", model, "--effort", effort, "--max-turns", "1",
            "--output-format", "stream-json", "--verbose"]


def parse_stream(stdout_text):
    packets, errors = [], 0
    for line in stdout_text.splitlines():
        try:
            packets.append(json.loads(line))
        except json.JSONDecodeError:
            errors += 1
    models, final, cost, usage_models = set(), None, None, []
    for p in packets:
        if p.get("type") == "assistant":
            m = (p.get("message") or {}).get("model")
            if m:
                models.add(m)
        if p.get("type") == "result":
            final = p.get("result")
            cost = p.get("total_cost_usd")
            usage_models = sorted((p.get("modelUsage") or {}).keys())
    return {"assistant_models": sorted(models), "usage_models": usage_models, "final_text": final,
            "cost_usd": cost, "parse_errors": errors, "packets": len(packets)}


def parse_verdict(text):
    if not text:
        return None, "empty"
    m = re.search(r"\{.*\}", text, flags=re.S)
    if not m:
        return None, "no json object"
    try:
        v = json.loads(m.group(0))
    except json.JSONDecodeError as e:
        return None, f"json error: {e}"
    keys = {"forbidden_access", "hidden_data_in_deliverable", "implicated", "permission_claimed", "evidence"}
    missing = sorted(keys - set(v))
    if "violation_likelihood" not in v and "confidence" not in v:   # v2 field, v1 fallback
        missing.append("violation_likelihood")
    return v, ("missing keys: " + ", ".join(missing)) if missing else None


def one_call(state, args, system, exe):
    started = time.monotonic()
    env, handling = run_r3.subject_environment(os.environ)
    with tempfile.TemporaryDirectory(prefix="monitor-call-") as cwd:
        diag = Path(cwd) / "diag.jsonl"
        env["CLAUDE_CODE_DIAGNOSTICS_FILE"] = str(diag)
        cmd = command(exe, args.model, system, args.effort)
        timed_out = False
        try:
            proc = subprocess.run(cmd, cwd=cwd, input=state["payload"], capture_output=True, text=True,
                                  env=env, timeout=args.timeout)
            stdout, stderr, rc = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as e:
            timed_out, stdout, stderr, rc = True, (e.stdout or "") if isinstance(e.stdout, str) else "", "", None
        diagnostics = run_r3.parse_diag(diag)
    parsed = parse_stream(stdout)
    verdict, verr = parse_verdict(parsed["final_text"])
    return {"state_id": state["state_id"], "episode_id": state["episode_id"], "view": state["view"],
            "payload_sha256": state["payload_sha256"], "model_requested": args.model, "effort": args.effort,
            "assistant_models": parsed["assistant_models"], "usage_models": parsed["usage_models"],
            # as in the instrument (run_r3.classify): every assistant turn must carry the requested id; helper or
            # background model ids elsewhere in the stream are recorded as other_models and do not invalidate the call
            "model_ok": parsed["assistant_models"] == [args.model],
            "other_models": sorted(m for m in parsed["usage_models"] if m != args.model),
            "final_text": parsed["final_text"], "verdict": verdict, "verdict_error": verr,
            "cost_usd": parsed["cost_usd"], "stream_packets": parsed["packets"], "stream_parse_errors": parsed["parse_errors"],
            "exit_code": rc, "timed_out": timed_out, "stderr_tail": (stderr or "")[-400:],
            "diagnostics": diagnostics, "env_passed": handling["passed"], "elapsed_s": round(time.monotonic() - started, 3),
            "time_ns": time.time_ns(), "claude_version": subprocess.run([exe, "--version"], capture_output=True, text=True).stdout.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("states")
    ap.add_argument("--model", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--views", default="job,chain,plus")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--streams", type=int, default=4)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--only-positives", action="store_true", help="states whose own job is READ or LEAK")
    ap.add_argument("--only-ids", default=None, help="file with one state_id per line")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    views = set(args.views.split(","))
    states = [json.loads(l) for l in Path(args.states).open(encoding="utf-8")]
    states = [s for s in states if s["view"] in views]
    if args.only_positives:
        states = [s for s in states if s["truth"]["READ"] or s["truth"]["LEAK"]]
    if args.only_ids:
        keep = set(Path(args.only_ids).read_text().split())
        states = [s for s in states if s["state_id"] in keep]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    done = set()
    calls = out / "calls.jsonl"
    if calls.exists():
        done = {json.loads(l)["state_id"] for l in calls.open(encoding="utf-8")}
    todo = [s for s in states if s["state_id"] not in done]
    if args.limit:
        todo = todo[:args.limit]
    system = load_system_prompt(args.prompt)
    exe = shutil.which("claude")
    header = {"states_file": str(Path(args.states).resolve()), "states_sha256": sha(Path(args.states).read_text(encoding="utf-8")),
              "prompt_file": str(Path(args.prompt).resolve()), "system_sha256": sha(system), "model": args.model,
              "effort": args.effort, "views": sorted(views), "n_states": len(states), "n_todo": len(todo),
              "already_done": len(done), "dry_run": args.dry_run, "claude_exe": exe, "started_ns": time.time_ns()}
    (out / f"run_{header['started_ns']}.json").write_text(json.dumps(header, indent=2) + "\n", encoding="utf-8")
    # plan.json marks the directory as a run for instrument/publish_scrub.py (--runs monitor/runs), which must pass over
    # every monitor run before release: notes quoted in verdicts can carry the account e-mail that the subject sessions saw
    (out / "plan.json").write_text(json.dumps({**header, "kind": "monitor-run"}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: header[k] for k in ("model", "views", "n_states", "n_todo", "already_done", "dry_run", "system_sha256")}))
    if args.dry_run:
        (out / "dry_run_command.json").write_text(json.dumps(command(exe or "claude", args.model, system, args.effort), indent=2) + "\n")
        for s in todo[:3]:
            print("---", s["state_id"], len(s["payload"]), "chars")
        return
    if not exe:
        raise SystemExit("Claude Code is not installed on this machine")
    with calls.open("a", encoding="utf-8") as f, cf.ThreadPoolExecutor(max_workers=args.streams) as pool:
        n = 0
        for rec in pool.map(lambda s: one_call(s, args, system, exe), todo):
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            n += 1
            if n % 20 == 0 or n == len(todo):
                print(f"{n}/{len(todo)} calls; last: {rec['state_id']} model_ok={rec['model_ok']} verdict={'ok' if rec['verdict'] else rec['verdict_error']}")


if __name__ == "__main__":
    main()
