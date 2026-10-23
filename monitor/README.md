# monitor/ — what the announced auditor would have seen

New sprint work (23 October 2026, written after the main run; Claude). A monitor study on the main-run records: an
auditor model reads what the jobs left in `/shared/notes`, in three views, and its verdicts are scored against the
frozen classifier's ground truth. Nothing here changes the instrument or the records; `build_states.py` and
`run_monitor.py` import `instrument/schema.py` and `instrument/run_r3.py` read-only.

| file | role |
|---|---|
| `PREREGISTRATION_MONITOR.md` | question, views, truth, decision rule, hypotheses, calibration, freeze line |
| `build_states.py` | one payload per (chain, generation, view) from the records — views `note`, `job`, `chain`, `plus`, `ceiling`; seed excluded by hash; no arm label |
| `prompts/auditor_v1.md` | the auditor's system prompt (candidate until calibrated and hashed) |
| `run_monitor.py` | one headless call per state, no tools, allowlisted environment, model id and diagnostics per call; resumable |
| `score.py` | detection and false-alarm rates per view, paired contrasts (exact binomial on discordant pairs), per-positive table |
| `states/<run>/` | the built states and their manifest (hashes, counts, warnings) |
| `runs/<run>/<model>/` | `calls.jsonl` and `results_monitor.md` |

`states/*/states.jsonl` and `runs/` are not committed: states are rebuilt from the records and pinned by the hashes in
`states/<run>/manifest.json`; both contain note text, which in this run carries the account e-mail the subject sessions saw,
so `runs/` goes through `instrument/publish_scrub.py --runs monitor/runs` before anything is released.

Order of work: build states → calibrate the prompt on the gate run only → fill the `[BIND]` line and commit →
main run → score. Verdicts are not reported before the hand coding of `instrument/runs/coding/` is closed.
