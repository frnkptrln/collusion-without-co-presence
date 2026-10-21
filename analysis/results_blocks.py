#!/usr/bin/env python3
# from peer-pressure-without-peers@9b048f1 (prior work); rewritten 2026-10 for the sprint design — the September paper
# placeholders are gone; the block mechanics (sections of results.md copied verbatim, missing runs named) are kept.
"""Assemble the results sheet for the report from the run directories — analysis side, no model call.

  python3 results_blocks.py <runs directory> [--out RESULTS_BLOCKS.md]

Reads results.md and reports/replacement_endpoints.json of the gate, re-gate, main and positive-control run directories and
writes one block per registered hypothesis in the order of PREREGISTRATION.md §6 (H0–H5, PC), each with the lines copied
verbatim from results.md and the file and line they come from, so that the author writes the report from a sheet and
every number can be traced to its line (check_quotes.py verifies quoted passages of ≥ 35 characters against the records,
not numbers; the line references here are the trace for the numbers). Every endpoint row carries its endpoint label
(G1 / PROP / PROP+ / CARRY) and its own line number, also where lines repeat (V10). A block whose run is missing says so
instead of pretending. No prose is drafted: the report is the author's own writing.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RUNS = {"gate": "gate — replacement chains (pilot seeds, never pooled)", "gate-B": "re-gate with hand-off wording B (fresh pilot seeds, never pooled)",
        "pc-gate": "gate — positive control", "main": "main — replacement chains", "pc-main": "main — positive control"}
ENDPOINTS_HEADING = "Chain endpoints (three-state: positive / negative / unknown — D5 rules; identification range [k/N, (k+u)/N] is not a confidence interval)"
REGISTERED_HEADING_PREFIX = "Registered tests and readings"
H5_HEADING_PREFIX = "H5 — provenance decay"
ORIGIN_DECAY_HEADING_PREFIX = "ORIGIN-DECAY (§5.2)"
PC_HEADING_PREFIX = "Positive control — the static cell that broke the model in September"


def sections(lines):
    """Split a results.md into {heading: (start_index, end_index)} over line indices (0-based, end exclusive) for headings
    of level 1–2; the first heading wins on duplicates."""
    out, cur, start = {}, None, 0
    for i, line in enumerate(lines):
        if line.startswith("#"):
            if cur is not None and cur not in out:
                out[cur] = (start, i)
            cur, start = line.lstrip("#").strip(), i + 1
    if cur is not None and cur not in out:
        out[cur] = (start, len(lines))
    return out


def load(runs: Path, name: str):
    d = runs / name
    if not (d / "results.md").exists():
        return None
    text = (d / "results.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    ep = d / "reports" / "replacement_endpoints.json"
    return {"dir": d, "name": name, "text": text, "lines": lines, "sections": sections(lines),
            "endpoints": json.loads(ep.read_text(encoding="utf-8")) if ep.exists() else None,
            "figures": sorted(str(p.relative_to(runs)) for p in (d / "reports").glob("*.png")) if (d / "reports").exists() else []}


def find_heading(r, prefix: str):
    return next((h for h in r["sections"] if h.startswith(prefix)), None)


def cite(r, pattern: str, within: str | None = None):
    """Every line of results.md matching `pattern` (regex), each with its own line number (1-based); `within` restricts
    the search to one section, given by its heading or a heading prefix."""
    lo, hi = 0, len(r["lines"])
    if within:
        heading = within if within in r["sections"] else find_heading(r, within)
        if heading is None:
            return [f"_section `{within}` not found in {r['name']}/results.md_"]
        lo, hi = r["sections"][heading]
    out = []
    for i in range(lo, hi):
        line = r["lines"][i]
        if re.search(pattern, line):
            out.append(f"{line}  \n  — `{r['name']}/results.md:{i + 1}`")
    return out or [f"_no line matching `{pattern}` in {r['name']}/results.md_"]


def section_block(r, heading: str):
    h = heading if heading in r["sections"] else find_heading(r, heading)
    if h is None:
        return [f"_section `{heading}` not found in {r['name']}/results.md_"]
    lo, hi = r["sections"][h]
    body = "\n".join(r["lines"][lo:hi]).strip()
    return [body, "", f"— `{r['name']}/results.md` lines {lo + 1}–{hi}"]


def block(title, body_lines):
    return [f"## {title}", ""] + body_lines + [""]


def missing(name):
    return [f"_run `{name}` not present — nothing to report_"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    runs = Path(a.runs).resolve()
    R = {k: load(runs, k) for k in RUNS}
    m = R["main"]
    L = [f"# RESULTS SHEET — assembled from `{runs}` (lines copied verbatim from results.md, each with its source line; no prose)", ""]
    L += block("Validity and the per-arm table (Table 1 of the report)",
               (section_block(m, "Per arm and generation") + [""] + section_block(m, "Note predicates — secondary columns") + [""] + cite(m, r"^Records: ")) if m else missing("main"))
    L += block("H0 — baseline: the empty arm (A0) over five generations",
               cite(m, r"^  - (G1|PROP|PROP\+|CARRY) A0: ", ENDPOINTS_HEADING) if m else missing("main"))
    L += block("H1 — replacement: PROP+ in the peer-note arm (A1), with provenance",
               (cite(m, r"^  - (G1|PROP|PROP\+|CARRY) A1: ", ENDPOINTS_HEADING)
                + cite(m, r"PROP\+, A1 peer note vs A2 record") + section_block(m, "Existence cases")) if m else missing("main"))
    L += block("H2 — carrier: generation-1 violation, peer note (A1) vs record (A2) — registered test and reading",
               cite(m, r"H2 ", REGISTERED_HEADING_PREFIX) if m else missing("main"))
    L += block("H3 — observation: the watched arm (A3) against the peer-note arm (A1) — registered tests and reading",
               cite(m, r"H3 ", REGISTERED_HEADING_PREFIX) if m else missing("main"))
    L += block("H4 — payload beyond text: PAYLOAD-CARRY, empty (A0) vs peer note (A1)",
               (cite(m, r"^  - CARRY A[01]: ", ENDPOINTS_HEADING) + cite(m, r"PAYLOAD-CARRY, A0 empty vs A1 peer note")
                + cite(m, r"^- (LEAK|STATUS_MISLABEL|fabrication) episodes")) if m else missing("main"))
    L += block("H5 — provenance decay: ORIGIN-DECAY (§5.2) by arm, and the A1 chains carrying the payload",
               (section_block(m, ORIGIN_DECAY_HEADING_PREFIX) + [""] + section_block(m, H5_HEADING_PREFIX)) if m else missing("main"))
    pc = R["pc-main"]
    L += block("PC — positive control (16 static episodes, new seeds)", section_block(pc, PC_HEADING_PREFIX) if pc else missing("pc-main"))
    gate_lines = []
    for name in ("gate", "gate-B"):
        g = R[name]
        if not g:
            gate_lines += missing(name) if name == "gate" else [f"_run `{name}` not present (no re-gate)_"]
            continue
        gate_lines += [f"{RUNS[name]} — pilot seeds; never pooled with the main design:"] + cite(g, r"^Records: ") + cite(g, r"^  - (G1|PROP|PROP\+|CARRY) A[0-3]: ", ENDPOINTS_HEADING)
        verdict = runs / ("GATE_VERDICT.json" if name == "gate" else "GATE_VERDICT_B.json")
        gate_lines += ["", f"Gate verdict ({verdict.name}):", "```", verdict.read_text(encoding="utf-8").strip() if verdict.exists() else f"_no {verdict.name} — was gate.py run?_", "```", ""]
    pg = R["pc-gate"]
    gate_lines += section_block(pg, PC_HEADING_PREFIX) if pg else missing("pc-gate")
    L += block("Gate (Thursday) — reported as preparation, never pooled", gate_lines)
    figs = [f for r in R.values() if r for f in r["figures"]]
    L += block("Figures", [f"- `{f}`" for f in figs] or ["- none"])
    out = Path(a.out) if a.out else runs / "RESULTS_BLOCKS.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    present = [k for k, v in R.items() if v]
    print(json.dumps({"out": str(out), "runs_present": present, "runs_missing": [k for k in RUNS if k not in present]}))


if __name__ == "__main__":
    main()
