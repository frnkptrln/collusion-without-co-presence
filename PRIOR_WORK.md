# Prior work in this repository

The sprint's rule: building on existing work is allowed, new sprint work must be clearly identified, undisclosed prior work can disqualify. This file is that identification.

## Source

`frnkptrln/peer-pressure-without-peers`, the instrument, run records and papers of "Peer pressure without peers" (Apart Research × CeSIA AI Incident Response Sprint, 11–13 September 2026). The copies here are taken from its submitted state, commit `9b048f1cf611e74e61a0230b6abbd978d0ed31a3` (14 September 2026), tag `submitted`; the later commits there only add the submitted-state note to its README and do not touch the files copied. Licence of the source: code MIT; papers, notes, fixtures and run records CC BY 4.0.

## Copied unchanged

Every file below carries, as its first comment line, `copied unchanged from peer-pressure-without-peers@9b048f1 (prior work)`; apart from that line the files are byte-identical to the source (checked by removing the line and diffing).

| here | there |
|---|---|
| `instrument/workspace_server.py`, `concern_server.py`, `fixtures_r3.py`, `run_r3.py`, `analyze_r3.py`, `schema.py`, `stats.py`, `report.py`, `freeze.py`, `quota.py`, `sprint_autorun.py`, `d4_gate.py` | `harness-r3/` |
| `instrument/tests/test_d4.py`, `test_d5.py`, `test_figures_rehearsal.py`, `test_r3_harness.py`, `test_review_regressions.py`, `test_tools.py` | `harness-r3/tests/` |
| `analysis/schema.py`, `stats.py`, `report.py`, `results_blocks.py`, `figures.py`, `coding_sheet.py`, `make_stub.py` | `analysis/` |
| `analysis/tests/test_figures.py`, `test_r3_analysis.py` | `analysis/tests/` |
| `report/build_apart.py`, `report/apart_template.tex` | `papers/` |

## Copied with path adaptations

Two files refer to the source repository's directory names (`harness-r3/`, `papers/`) and were adapted to this layout (`instrument/`, `report/`); nothing else in them changed: `instrument/check_quotes.py` (the three path constants and two usage strings), `instrument/publish_scrub.py` (the container-path pattern accepts `instrument` beside `harness-r3`; one docstring line).

## Left out, and why

- `harness-r3/sweep_e4.py`, `run_open_r3.py`, `open_tier/` and their tests `test_d3.py`, `test_open_r3.py`; `analysis/e4_answerline.py` and `test_e4_answerline.py`: the declarative survey and the open-weights tier are not part of this design. `test_d3.py` also carried two tests of the descriptive interaction line in `report.py`; that function is unchanged here but those two tests are not copied.
- `harness-r3/runs/` (every September episode), `MANIFEST.sha256.*.json`, `DEVIATIONS.md`, `AMENDMENT_r3.md`, `RUNBOOK_sprint.md`, the papers, `review/`, `SOURCES.md`, `PACKAGE_STATE.md`: September's evidence, freeze and texts stay in their own repository and are cited, not copied. The September test `test_tools.py` skips its coding-pipeline case when the `e1-gate` run is absent, as it is here.

## New sprint work

Everything that is not in the tables above is new for this sprint and dated October 2026: the pre-registration and plan, the documents in this repository, and — in the code — every block marked `NEW 2026-10`. The September files that the sprint design changes lose their "copied unchanged" line at that change and keep a note of what changed and why.
