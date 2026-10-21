# from peer-pressure-without-peers@9b048f1 (prior work); rewritten 2026-10 for the sprint design — the September phases
# (friday / saturday / d4) and paper blocks are gone; the same three tool paths are exercised for the new phases.
"""The sprint tooling outside the frozen instrument, exercised without a model: the autonomous runner (gate phase with
its verdict, main phase, restartability, the analysis-only phase, the wording-B fallback as an argument), the results
sheet, and the coding sheet / model-coder stub / κ pipeline on rehearsal episodes."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ANALYSIS = ROOT.parent / "analysis"
PY = sys.executable


def run(args, cwd=ROOT):
    return subprocess.run([PY] + [str(a) for a in args], cwd=cwd, capture_output=True, text=True)


class TestAutorun(unittest.TestCase):
    def test_gate_phase_verdict_and_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "gate", "--backend", "rehearsal", "--runs", tmp, "--rehearsal-policy", "chain_payload"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("gate: **PASS**", r.stdout)
            self.assertIn("phase gate done", r.stdout)
            self.assertEqual(sum(1 for _ in (Path(tmp) / "gate").glob("e3-gate-*/result.json")), 40)
            self.assertEqual(sum(1 for _ in (Path(tmp) / "pc-gate").glob("e1-gate-*/result.json")), 4)
            self.assertTrue((Path(tmp) / "GATE_VERDICT.json").exists())
            verdict = json.loads((Path(tmp) / "GATE_VERDICT.json").read_text(encoding="utf-8"))
            self.assertEqual((verdict["claude_code_versions"], verdict["other_models"]), ({}, {}))   # scripted: nothing recorded, keys present (V4, V8)
            self.assertTrue((Path(tmp) / "gate" / "reports" / "replacement_report.md").exists())
            r2 = run([ROOT / "sprint_autorun.py", "--phase", "gate", "--backend", "rehearsal", "--runs", tmp])
            self.assertEqual(r2.returncode, 0, r2.stderr)
            self.assertIn("already prepared — resuming", r2.stdout)           # restart: nothing rerun
            self.assertEqual(sum(1 for _ in (Path(tmp) / "gate").glob("e3-gate-*/result.json")), 40)
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "gate", "--backend", "rehearsal", "--runs", tmp, "--rehearsal-policy", "no_notes"])
            self.assertEqual(r.returncode, 0, r.stderr)                        # a failed gate is a verdict, not a crash
            self.assertIn("gate: **FAIL**", r.stdout)
            self.assertIn("fallback (not executed", r.stdout)
            self.assertIn("wording B", r.stdout)

    def test_main_phase_and_results_sheet_and_analysis(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "main", "--backend", "rehearsal", "--runs", tmp, "--handoff", "B", "--rehearsal-policy", "chain_payload"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("phase main done", r.stdout)
            self.assertEqual(sum(1 for _ in (Path(tmp) / "main").glob("e3-main-*/result.json")), 320)
            self.assertEqual(sum(1 for _ in (Path(tmp) / "pc-main").glob("e1-main-*/result.json")), 16)
            plan = json.loads((Path(tmp) / "main" / "plan.json").read_text(encoding="utf-8"))
            self.assertEqual(plan["handoff"], "B")
            self.assertTrue((Path(tmp) / "main" / "results.md").exists())
            r = run([ANALYSIS / "results_blocks.py", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            text = (Path(tmp) / "RESULTS_BLOCKS.md").read_text(encoding="utf-8")
            for heading in ("## H0 — baseline", "## H1 — replacement", "## H2 — carrier", "## H3 — observation", "## H4 — payload", "## H5 — provenance decay", "## PC — positive control"):
                self.assertIn(heading, text)
            self.assertIn("main/results.md:", text)
            self.assertIn("run `gate` not present", text)
            r = run([ROOT / "sprint_autorun.py", "--phase", "analysis", "--backend", "rehearsal", "--runs", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("analysis phase done", r.stdout)


class TestCodingPipeline(unittest.TestCase):
    def test_sheet_stub_kappa_on_rehearsal_episodes(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "gate", "--backend", "rehearsal", "--runs", tmp, "--rehearsal-policy", "chain_payload"])
            self.assertEqual(r.returncode, 0, r.stderr)
            gate = Path(tmp) / "gate"
            out = Path(tmp) / "coding"
            r = run([ANALYSIS / "coding_sheet.py", "sheet", gate, "--n", "8", "--seed", "3", "--out", out])
            self.assertEqual(r.returncode, 0, r.stderr)
            info = json.loads(r.stdout)
            self.assertEqual(len(info["episodes"]), 8)
            self.assertEqual(info["strata"], ["A0", "A1", "A2", "A3"])
            rows = list(csv.DictReader((out / "sheet.csv").open(encoding="utf-8")))
            self.assertEqual(len(rows), 8)
            self.assertNotIn("arm", rows[0])                                     # blinded
            key = json.loads((out / "sheet_key.json").read_text(encoding="utf-8"))
            self.assertEqual(sorted(key), sorted(r["episode_id"] for r in rows))
            self.assertEqual(sum(1 for v in key.values() if v["arm"] == "A1"), 2)
            for row in rows:
                t = (out / row["transcript"]).read_text(encoding="utf-8")
                self.assertIn("## Notes this agent wrote", t)
            r = run([ANALYSIS / "coding_sheet.py", "code", out, "--backend", "stub"])
            self.assertEqual(r.returncode, 0, r.stderr)
            rows = list(csv.DictReader((out / "sheet.csv").open(encoding="utf-8")))
            self.assertTrue(all(row["model_origin_named"] in ("yes", "no") for row in rows))
            for row in rows:                                                     # a human coder who agrees with the instrument
                mech = key[row["episode_id"]]["mechanical"]
                for ax in ("origin_named", "authorization_claimed", "payload_present"):
                    row["human_" + ax] = mech[ax]
                row["human_handoff_explicit_about_rule"] = "1"
            with (out / "sheet.csv").open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)
            r = run([ANALYSIS / "coding_sheet.py", "kappa", out / "sheet.csv", "--b", "mechanical"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("| origin_named | 8 | 1.00 |", r.stdout)
            self.assertIn("| A1 | 6 | 1.00 |", r.stdout)
            r = run([ANALYSIS / "coding_sheet.py", "kappa", out / "sheet.csv"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("Coders: `human_*` vs `model_*`", r.stdout)


if __name__ == "__main__":
    unittest.main()
