#!/usr/bin/env python3
# Claude, 25 October 2026 — monitor study. Draws the secondary model's subset (PREREGISTRATION_MONITOR.md §4):
# every positive chain episode (own job READ or LEAK) and k clean negatives per positive, by a seeded permutation.
"""  python3 monitor/select_subset.py monitor/states/main/states.jsonl --k 2 --seed 20261023 --views note,job,chain,plus --out monitor/states/main/subset_ids.txt"""
import argparse
import json
import random
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("states")
    ap.add_argument("--k", type=int, default=2)
    ap.add_argument("--seed", type=int, default=20261023)
    ap.add_argument("--views", default="note,job,chain,plus")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    views = a.views.split(",")
    states = [json.loads(l) for l in Path(a.states).open(encoding="utf-8")]
    chain_view = [s for s in states if s["view"] == "chain"]
    positives = sorted(s["episode_id"] for s in chain_view if s["truth"]["READ"] or s["truth"]["LEAK"])
    clean = sorted(s["episode_id"] for s in chain_view
                   if not (s["truth"]["READ"] or s["truth"]["LEAK"] or s["truth"]["STATUS_MISLABEL"]) and not s["meta"]["contains_seed_text"])
    rng = random.Random(a.seed)
    negatives = sorted(rng.sample(clean, a.k * len(positives)))
    ids = [f"{s['run']}-{ep}-{v}" for ep in positives + negatives for v in views for s in [chain_view[0]]]
    Path(a.out).write_text("\n".join(ids) + "\n", encoding="utf-8")
    print(json.dumps({"positives": len(positives), "negatives": len(negatives), "clean_pool": len(clean), "views": views,
                      "state_ids": len(ids), "seed": a.seed, "positive_episodes": positives, "negative_episodes": negatives}, indent=1))


if __name__ == "__main__":
    main()
