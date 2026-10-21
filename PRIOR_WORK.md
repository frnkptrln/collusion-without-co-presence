# Prior work in this repository

The sprint's rule: building on existing work is allowed, new sprint work must be clearly identified, undisclosed prior work can disqualify. This file is that identification.

## Source

`frnkptrln/peer-pressure-without-peers`, the instrument, run records and papers of "Peer pressure without peers" (Apart Research × CeSIA AI Incident Response Sprint, 11–13 September 2026). The copies here are taken from its submitted state, commit `9b048f1cf611e74e61a0230b6abbd978d0ed31a3` (14 September 2026), tag `submitted`; the later commits there only add the submitted-state note to its README and do not touch the files copied. Licence of the source: code MIT; papers, notes, fixtures and run records CC BY 4.0.

## Copied unchanged

Every file below carries, as its first comment line, `copied unchanged from peer-pressure-without-peers@9b048f1 (prior work)`; apart from that line the files are byte-identical to the source (checked by removing the line and diffing).

| here | there |
|---|---|
| `instrument/workspace_server.py`, `concern_server.py`, `fixtures_r3.py`, `run_r3.py`, `analyze_r3.py`, `schema.py`, `stats.py`, `report.py`, `freeze.py`, `sprint_autorun.py`, `d4_gate.py` | `harness-r3/` |
| `instrument/tests/test_d4.py`, `test_d5.py`, `test_figures_rehearsal.py`, `test_r3_harness.py`, `test_review_regressions.py`, `test_tools.py` | `harness-r3/tests/` |
| `analysis/schema.py`, `stats.py`, `report.py`, `results_blocks.py`, `figures.py`, `coding_sheet.py`, `make_stub.py` | `analysis/` |
| `analysis/tests/test_figures.py`, `test_r3_analysis.py` | `analysis/tests/` |
| `report/build_apart.py`, `report/apart_template.tex` | `papers/` |

## Copied with path adaptations

Two files refer to the source repository's directory names (`harness-r3/`, `papers/`) and were adapted to this layout (`instrument/`, `report/`): `instrument/check_quotes.py` (the three path constants and two usage strings; nothing else changed), `instrument/publish_scrub.py` (the container-path pattern accepts `instrument` beside `harness-r3`; one docstring line — and, on 21 October, every UTF-8 file under the runs root is scrubbed whatever its extension, the path pattern covers any `/home/<user>` and `/Users/<user>` prefix, and the redaction record counts the files it could not decode; see the file's header).

## Left out, and why

- `harness-r3/sweep_e4.py`, `run_open_r3.py`, `open_tier/` and their tests `test_d3.py`, `test_open_r3.py`; `analysis/e4_answerline.py` and `test_e4_answerline.py`: the declarative survey and the open-weights tier are not part of this design. `test_d3.py` also carried two tests of the descriptive interaction line in `report.py`; that function is unchanged here but those two tests are not copied.
- `harness-r3/runs/` (every September episode), `MANIFEST.sha256.*.json`, `DEVIATIONS.md`, `AMENDMENT_r3.md`, `RUNBOOK_sprint.md`, the papers, `review/`, `SOURCES.md`, `PACKAGE_STATE.md`: September's evidence, freeze and texts stay in their own repository and are cited, not copied. The September test `test_tools.py` skips its coding-pipeline case when the `e1-gate` run is absent, as it is here.

## Changed for the sprint design (October 2026)

These September files were changed for the replacement design; each carries a first-line note instead of the "copied unchanged" line, and every change inside is marked `NEW 2026-10`: `instrument/fixtures_r3.py` (seed `T3x1`, hand-off and audit texts, arms, designs `replacement` and `pc`), `run_r3.py` (CLI, `initial_notes` in `materialized.json`, rehearsal policy `chain_payload`), `analyze_r3.py` (note predicates, read order, inherited payload), `schema.py` (the `LEAK` overlay), `report.py` (the replacement report, the positive-control section), `freeze.py` (this repository's instrument list and pre-registration), `sprint_autorun.py` (rewritten: phases `gate`, `main`, `analysis`, `check`; the re-gate `gate-B`), `quota.py` (21 October: the run root resolved against `instrument/`, not the working directory), `tests/test_tools.py` (rewritten for those phases); `analysis/schema.py` and `analysis/report.py` (kept identical to the instrument's copies), `analysis/figures.py` (the replacement figure), `analysis/results_blocks.py` (rewritten: the results sheet of PREREGISTRATION.md §6), `analysis/coding_sheet.py` (the note-content axes, blinded sheet, mechanical comparison). Removed: `instrument/d4_gate.py` (the September continuation gate; this design has no outcome-dependent stopping — `gate.py` is the Thursday gate of §4.6). New: `instrument/gate.py`, `instrument/tests/test_replacement.py`, `analysis/tests/test_replacement_analysis.py`.

## Unreleased prior work

On 10 September 2026 a working line of the September instrument — design D7, "chain-seeded-handoff": the D4 seeded chains on Haiku 4.5 plus one neutral hand-off sentence in the task README — was run: 80 episodes, notes in 78/80, generation-1 violation 4/8 seeded vs 0/8 unseeded, an effect beyond generation 1 in 3 of the 4 violating chains, five later agents delivering the full totals without reading the forbidden file (leak-completions), source-naming in the notes decaying over generations while the totals persisted. This run is *not* disclosed in the published September papers, which disclose only that line's D4 execution (the released seeded run that stopped after generation 1); its records are unreleased and are in no public repository. The hand-off sentence of this sprint's design (`HANDOFF["A"]` in `instrument/fixtures_r3.py`) derives from it. `PREREGISTRATION.md` §2 and §11 cite it as prior observation, never as data; whether its records are released is Frank's decision and is not made here. (Written 21 October 2026.)

## New sprint work

Everything that is not in the tables above is new for this sprint and dated October 2026: the pre-registration and plan, the documents in this repository, and — in the code — every block marked `NEW 2026-10`.
