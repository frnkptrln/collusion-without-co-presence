#!/usr/bin/env python3
# from peer-pressure-without-peers@9b048f1 (prior work); rewritten 2026-10 for the sprint design — the September paper
# placeholders are gone; the block mechanics (sections of results.md copied verbatim, missing runs named) are kept.
"""Assemble the results sheet for the report from the run directories — analysis side, no model call.

  python3 results_blocks.py <runs directory> [--out RESULTS_BLOCKS.md]

Reads results.md and reports/replacement_endpoints.json of the gate, main and positive-control run directories and
writes one block per registered hypothesis in the order of PREREGISTRATION.md §6 (H0–H5, PC), each with the lines copied
verbatim from results.md and the file and line they come from, so that the author writes the report from a sheet and
check_quotes.py can verify every number. A block whose run is missing says so instead of pretending. No prose is drafted:
the report is the author's own writing.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RUNS = {"gate": "gate — replacement chains (pilot seeds, never pooled)", "pc-gate": "gate — positive control",
        "main": "main — replacement chains", "pc-main": "main — positive control"}


def sections(text: str) -> dict[str, str]:
    """Split a results.md into {heading: body} (headings of level 1–2; the first heading wins on duplicates)."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith("#"):
            if cur is not None and cur not in out:
                out[cur] = "\n".join(buf).strip()
            cur, buf = line.lstrip("#").strip(), []
        else:
            buf.append(line)
    if cur is not None and cur not in out:
        out[cur] = "\n".join(buf).strip()
    return out


def load(runs: Path, name: str):
    d = runs / name
    if not (d / "results.md").exists():
        return None
    text = (d / "results.md").read_text(encoding="utf-8")
    ep = d / "reports" / "replacement_endpoints.json"
    return {"dir": d, "name": name, "text": text, "lines": text.splitlines(), "sections": sections(text),
            "endpoints": json.loads(ep.read_text(encoding="utf-8")) if ep.exists() else None,
            "figures": sorted(str(p.relative_to(runs)) for p in (d / "reports").glob("*.png")) if (d / "reports").exists() else []}


def cite(r, pattern: str, within: str | None = None):
    """Every line of results.md matching `pattern` (regex), each with its line number; optionally only inside a section."""
    out = []
    hay = r["sections"].get(within, "") if within else r["text"]
    for line in hay.splitlines():
        if re.search(pattern, line):
            n = next((i + 1 for i, l in enumerate(r["lines"]) if l == line), None)
            out.append(f"{line}  \n  — `{r['name']}/results.md:{n}`" if n else line)
    return out


def section_block(r, heading: str):
    body = r["sections"].get(heading)
    if body is None:
        return [f"_section `{heading}` not found in {r['name']}/results.md_"]
    start = next((i + 1 for i, l in enumerate(r["lines"]) if l.lstrip("#").strip() == heading), None)
    return [body, "", f"— `{r['name']}/results.md` from line {start}"]


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
               (section_block(m, "Per arm and generation") + [""] + cite(m, r"^Records: ")) if m else missing("main"))
    L += block("H0 — baseline: the empty arm (A0) over five generations",
               cite(m, r"^  - A0: ", "Chain endpoints (three-state: positive / negative / unknown — D5 rules; identification range [k/N, (k+u)/N] is not a confidence interval)") if m else missing("main"))
    L += block("H1 — replacement: PROP+ in the peer-note arm (A1), with provenance",
               (cite(m, r"^  - A1: ", "Chain endpoints (three-state: positive / negative / unknown — D5 rules; identification range [k/N, (k+u)/N] is not a confidence interval)")
                + cite(m, r"H1 replacement") + section_block(m, "Existence cases")) if m else missing("main"))
    L += block("H2 — carrier: generation-1 violation, peer note (A1) vs record (A2)", cite(m, r"H2 carrier") if m else missing("main"))
    L += block("H3 — observation: the watched arm (A3) against the peer-note arm (A1)",
               (cite(m, r"H3 observation") + section_block(m, "H3 — which registered reading the watched arm matched (mechanical; the author's reading of the A3 notes is the primary qualitative evidence)")) if m else missing("main"))
    L += block("H4 — payload beyond text: PAYLOAD-CARRY, empty (A0) vs peer note (A1)",
               (cite(m, r"^  - A[01]: ", "Chain endpoints (three-state: positive / negative / unknown — D5 rules; identification range [k/N, (k+u)/N] is not a confidence interval)")
                + cite(m, r"H4 payload") + cite(m, r"^- LEAK episodes")) if m else missing("main"))
    L += block("H5 — provenance decay: notes naming the source by generation (A1, A3)",
               section_block(m, "ORIGIN decay — notes naming the source, by arm and generation (H5; share of written notes, Clopper–Pearson 95%)") if m else missing("main"))
    pc = R["pc-main"]
    L += block("PC — positive control (16 static episodes, new seeds)",
               section_block(pc, "Positive control — the static cell that broke the model in September (scorer + final attempt + three violating notes), new seeds") if pc else missing("pc-main"))
    g, pg = R["gate"], R["pc-gate"]
    gate_lines = []
    if g:
        gate_lines += ["Gate chains (pilot seeds; never pooled with the main design):"] + cite(g, r"^Records: ") + cite(g, r"^  - A[0-3]: ", "Chain endpoints (three-state: positive / negative / unknown — D5 rules; identification range [k/N, (k+u)/N] is not a confidence interval)")
        verdict = runs / "GATE_VERDICT.json"
        gate_lines += ["", "Gate verdict:", "```", verdict.read_text(encoding="utf-8").strip() if verdict.exists() else "_no GATE_VERDICT.json — was gate.py run?_", "```"]
    else:
        gate_lines += missing("gate")
    gate_lines += ([""] + section_block(pg, "Positive control — the static cell that broke the model in September (scorer + final attempt + three violating notes), new seeds")) if pg else missing("pc-gate")
    L += block("Gate (Thursday) — reported as preparation, never pooled", gate_lines)
    figs = [f for r in R.values() if r for f in r["figures"]]
    L += block("Figures", [f"- `{f}`" for f in figs] or ["- none"])
    out = Path(a.out) if a.out else runs / "RESULTS_BLOCKS.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    present = [k for k, v in R.items() if v]
    print(json.dumps({"out": str(out), "runs_present": present, "runs_missing": [k for k in RUNS if k not in present]}))


if __name__ == "__main__":
    main()
