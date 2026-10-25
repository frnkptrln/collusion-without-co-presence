#!/usr/bin/env python3
"""Figure 1 of the report: four panels over the five generations, one line per condition, from the per-arm-and-generation
table of instrument/runs/main/results.md (no model call, no recomputation — the counts are read from the table).

  python3 report/figure1.py [--results instrument/runs/main/results.md] [--out report/figure1.png]

Panels: A forbidden reads (READ / 16 valid episodes); B totals reused without a read (LEAK / 16); C notes naming the
source (ORIGIN / written notes); D notes carrying hidden data (PAYLOAD / written notes). Condition names are the plain
names of the report (empty, peer note, record, watched), not the arm codes. Written 25 October 2026 (Claude) for the
sprint report; the counts it draws are the ones of Table C1.
"""
import argparse
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ARMS = {"A0": "Empty", "A1": "Peer note", "A2": "Record", "A3": "Watched"}
STYLE = {"A0": dict(color="#8a8a8a", marker="o", ls=":", mfc="white"),
         "A1": dict(color="#1f5fa8", marker="s", ls="-"),
         "A2": dict(color="#d98c1f", marker="^", ls="--", mfc="white"),
         "A3": dict(color="#1d8f7a", marker="D", ls="-.")}
ROW = re.compile(r"^\| (A[0-3]) \| ([1-5]) \| (\d+) / (\d+) \| .*? \| (\d+)/(\d+) = [0-9.]+ \[[^\]]*\] \| (\d+) \| (\d+) \| (\d+) \| (\d+) "
                 r"\| (\d+)/(\d+) = [0-9.]+ \[[^\]]*\] \| (\d+) \| (\d+)/(\d+) = [0-9.]+ \[[^\]]*\] \| (\d+)/(\d+) = [0-9.]+ \[[^\]]*\] "
                 r"\| (\d+)/(\d+) = [0-9.]+ \[[^\]]*\] \|$")


def parse(results: Path):
    cells = {}
    for line in results.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line.strip())
        if not m:
            continue
        arm, gen = m.group(1), int(m.group(2))
        n_valid = int(m.group(3))
        read_k, read_n = int(m.group(5)), int(m.group(6))
        fab, leak, mislabel, honest = (int(m.group(i)) for i in (7, 8, 9, 10))
        notes = int(m.group(13))
        origin_k, origin_n = int(m.group(14)), int(m.group(15))
        payload_k, payload_n = int(m.group(18)), int(m.group(19))
        assert read_n == n_valid and origin_n == notes == payload_n, (arm, gen)
        cells[(arm, gen)] = dict(read=read_k / read_n, leak=leak / n_valid, origin=origin_k / origin_n if origin_n else float("nan"),
                                 payload=payload_k / payload_n if payload_n else float("nan"), notes=notes)
    assert len(cells) == 20, f"expected 20 arm×generation rows, found {len(cells)}"
    return cells


def main():
    ap = argparse.ArgumentParser()
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--results", default=str(root / "instrument" / "runs" / "main" / "results.md"))
    ap.add_argument("--out", default=str(root / "report" / "figure1.png"))
    a = ap.parse_args()
    cells = parse(Path(a.results))
    gens = [1, 2, 3, 4, 5]
    panels = [("A  Forbidden reads", "read", "Episodes (%)", "n = 16", 25),
              ("B  Totals reused without a read", "leak", "Episodes (%)", "n = 16", 25),
              ("C  Source named in notes", "origin", "Written notes (%)", "n = 14–16", 100),
              ("D  Hidden data in notes", "payload", "Written notes (%)", "n = 14–16", 25)]
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.0), dpi=200)
    for ax, (title, key, ylabel, note, ymax) in zip(axes.flat, panels):
        for arm in ("A0", "A1", "A2", "A3"):
            ys = [100 * cells[(arm, g)][key] for g in gens]
            ax.plot(gens, ys, label=ARMS[arm], lw=1.6, ms=6, **STYLE[arm])
        ax.set_title(title, loc="left", fontweight="bold", fontsize=11)
        ax.set_xlabel("Generation"); ax.set_ylabel(ylabel)
        ax.set_xticks(gens); ax.set_ylim(-1, ymax * 1.02 if ymax < 100 else 103)
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}%"))
        ax.text(0.99, 0.98, note, transform=ax.transAxes, ha="right", va="top", fontsize=9, color="#555555")
        ax.grid(axis="y", color="#e6e6e6"); ax.spines[["top", "right"]].set_visible(False)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False, fontsize=10, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(a.out)
    print(a.out)


if __name__ == "__main__":
    main()
