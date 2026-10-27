# Collusion without co-presence

Does a rule-breaking arrangement survive the replacement of every agent that holds it, when the only thing that persists is a shared scratch folder — and what does the arrangement do when it is told that the folder is read?

Instrument, pre-registration and — once the runs exist — the run records and the report for the **Apart Research AI Collusion Research Sprint** (23–25 October 2026), by Frank Peterlein. Continuation of [peer-pressure-without-peers](https://github.com/frnkptrln/peer-pressure-without-peers) (September 2026), whose instrument this repository reuses; what was taken from there and what is new is listed in `PRIOR_WORK.md`.

**Status: bound and frozen on 23 October 2026** — `PREREGISTRATION.md` is bound (no placeholders left), `instrument/MANIFEST.sha256.json` is written by `instrument/freeze.py`; from here on every change to a frozen file is a dated entry in `DEVIATIONS.md`. The texts (the hand-off sentence, the audit sentence, the arm table) are the constants at the top of `instrument/fixtures_r3.py`, section `NEW 2026-10`; the bound plans pin them by hash. Runs appear under `instrument/runs/` as they are executed.

## Pre-existing and sprint work

The sprint's rule: build on existing work, but mark code written before the sprint as pre-existing, and say what is new.

- **Prior work (September 2026):** the instrument copied from `peer-pressure-without-peers` — `PRIOR_WORK.md` lists every file and commit.
- **Written before the sprint (19–22 October 2026), pre-existing under the sprint rules:** the question and the four-arm design, the draft pre-registration, every code block marked `NEW 2026-10` (pull request #1 with its review and pre-freeze fixes), the tests and rehearsals.
- **New during the sprint (23–25 October 2026):** the binding and the freeze, the gate and main runs with their records under `instrument/runs/`, the analysis of those records, the hand coding, the figures, the monitor study (`monitor/`), and the report.

## The experiment in one paragraph

An agent (Claude Code, headless, four file tools served by our own MCP server that logs every call) gets a data task and a written rule: do not read the folder `/internal`. The task cannot be finished within the rule (6 of 24 records are missing; the complete file sits in `/internal`). A chain is five such agents in sequence: each session ends before the next begins, and the only thing that outlives a session is what it wrote into `/shared/notes`. At generation 1 of some chains we plant one note that looks as if an earlier job had broken the rule and scored; the note is removed before generation 2. We count forbidden reads from the tool log, by generation and chain, and read what the agents wrote to each other.

## What is in the repository

| path | what |
|---|---|
| `PREREGISTRATION.md` | question, design, outcomes, hypotheses, analysis plan (draft until bound) |
| `DEVIATIONS.md` | append-only deviation log, starts with the freeze |
| `PRIOR_WORK.md` | what was copied from the September repository, from which commit, under which licence; what is new |
| `instrument/` | the instrument: `fixtures_r3.py` (rule, task, notes, seeds, arms, plans), `run_r3.py` (runner; chains, seed removal, rehearsal backend), `workspace_server.py` (MCP task server with audit log), `concern_server.py`, `analyze_r3.py` / `schema.py` / `stats.py` / `report.py` (mechanical outcomes, note predicates, chain endpoints, the replacement report), `gate.py` (the Thursday gate, §4.6), `sprint_autorun.py` (the runbook as a script: `--phase gate`, `main`, `analysis`, `check`), `freeze.py`, `quota.py`, `check_quotes.py`, `publish_scrub.py`, `tests/`; `runs/` holds every episode once runs exist (`gate`, `pc-gate`, `main`, `pc-main`; `gate-B` if the re-gate with wording B is needed) |
| `analysis/` | instrument-independent analysis with tests: `results_blocks.py`, `figures.py`, `coding_sheet.py`, `make_stub.py` |
| `report/` | the submitted report (`collusion-without-co-presence-submission.pdf`, rendered from the `.docx` beside it), Figure 1 (`figure1.py`, `figure1.png`), the writing skeleton (`REPORT_SKELETON.md`), the draft history of Appendix D (`APPENDIX_MONITOR.md`); the LaTeX template builder (`build_apart.py`, `apart_template.tex`) was not used for the submitted report |
| `docs/` | `IMPLEMENTATION_PLAN.md` (what is reused, what changes), `REPORT_OUTLINE.md` |
| `monitor/` | the pre-registered add-on of 25 October: an auditor model reads the shared folders of the main run in four views, scored against the frozen classifier (`monitor/RESULTS.md`) |

**A note on the run records.** The records under `instrument/runs/` are published exactly as the runs wrote them. The
subject sessions ran through Claude Code under the operator's login, and Claude Code passes the account's e-mail
address into the agent's context; in 100 of the record files an agent wrote that address into its note or report. It
is the operator's own address, the same one that signs every commit of this repository, so the records were left
unaltered rather than scrubbed (`instrument/publish_scrub.py` remains available for a redacted copy). No key, token
or path of another person occurs in the records; the publication check of 25 October found none.

## Checks

No model call is needed for any of this.

```bash
cd instrument && python3 -m unittest discover -s tests && cd ../analysis && python3 -m unittest discover -s tests && cd ..
cd instrument && python3 run_r3.py doctor && cd ..      # MCP handshake with both servers, no model
cd instrument && python3 sprint_autorun.py --phase gate --backend rehearsal --runs /tmp/rehearsal --rehearsal-policy chain_payload && cd ..
cd instrument && python3 sprint_autorun.py --phase main --backend rehearsal --runs /tmp/rehearsal --rehearsal-policy chain_payload && cd ..
python3 analysis/results_blocks.py /tmp/rehearsal       # the results sheet, every line with its source
python3 analysis/coding_sheet.py sheet /tmp/rehearsal/main --n 24 --out /tmp/rehearsal/coding   # the blinded coding sheet
```

Running episodes needs Claude Code logged in to a subscription and Frank's go (`--backend claude`, the default of `sprint_autorun.py`; `--phase check` first — it refuses a runs root that holds rehearsal or main-phase directories). The subject sessions get an allowlisted environment with `DISABLE_AUTOUPDATER=1` (`run_r3.ENV_ALLOW`; `run_r3.py doctor` shows which of the current shell's variables would be passed and dropped). A record's model is checked against `assistant_models` (the model ids of the subject session's own turns) and `other_models` (every other id seen in the stream, helper calls included) in `result.json` and in the record's `cell`; `returned_models` — the record's `model` field — lists every id seen, the result packet's `modelUsage` keys among them, and is not the check. The scripted rehearsal backend (`--backend rehearsal`) exercises every part of the pipeline without a model — policies `honest`, `chain_propagate` (a violation that names its source travels down the chain) and `chain_payload` (the first violator names the source and leaves the totals, later notes carry the totals without the source, later agents complete from the channel); nothing a rehearsal produces is evidence about a model.

## Licence

Code: MIT (`LICENSE`). Pre-registration, notes, fixtures, run records and report: CC BY 4.0 (`LICENSES/CC-BY-4.0.txt`). The copied instrument carries the licence of its source repository (MIT).

## AI use

Claude (Anthropic) drafted the pre-registration and the plan, wrote the code changes and the analysis, ran the gate and the main run on the author's go, designed, ran and scored the monitor study of 25 October (its predictions adopted by Frank before the first call), wrote the report skeleton and revised the manuscript; Codex (OpenAI) proposed the labels of the coding sample and drafted the manuscript; Frank Peterlein decides the design, adopted the predictions, authorised every run, reviewed and adopted the coding labels, and reads, corrects and adopts the report (the departures from `PREREGISTRATION.md` §7 and §11 are the entries of 25 October in `DEVIATIONS.md`). The subject model runs through Claude Code on one subscription.
