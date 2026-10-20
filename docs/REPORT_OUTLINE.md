# Report outline — slots, not prose

The report is Frank's own writing about his own work (sprint rule: AI tools for checking reasoning, finding gaps and debugging; "generated-looking" reports are not scored — Reviewer 1 of the September submissions wrote exactly that). This outline lists what each section must contain and which number from `results_blocks.py` goes where. No sentence here is meant to be copied.

Hard requirements from the sprint page (re-check the Guidelines tab on 22 October): official PDF template; 4–8 pages is the typical strong length; title and abstract ≤ 150 words; author and affiliation; a **Limitations and Dual-Use / Ethical Considerations appendix** (required: what the result does and does not establish; whether the work could make collusion easier to carry out or harder to detect); results with variance, seeds, baselines and a positive control; prior work clearly separated from new sprint work; sources linked for factual claims; optional public repository and 3–5 minute video.

Three rules from the September reviews, applied to every section:
1. **No condition codes in the main text.** Write "the empty-folder chains", "the peer-note chains", "the record chains", "the watched chains", "generation 1 / later generations". Codes (A0–A3, G1, PROP+) live in the repository, not in the report.
2. **Hedging goes to the limitations section**, once. The results section states what was observed.
3. **Findings are not weaker than the framing.** If the arrangement did not propagate, the title's question is answered "no, not here" in the abstract.

## Title
Working title: *Collusion without co-presence: can a planted rule violation outlive every agent that held it?* — adjust after the data (a question in the title must be answered in the abstract).

## Abstract (≤ 150 words)
Question in one sentence; instrument in one sentence (fresh agent per generation, shared folder the only continuity, one violating note planted once); the four arms in one sentence; the main numbers: generation-1 violation by arm, chains with a provenance-backed later violation, leak-completions, what the audit notice did; one sentence of limits (one model, one tier, 16 chains per arm).

## 1. Introduction (½ page)
Why replacement matters for collusion (Track 1.2 asks about replacing some participants; here all are replaced). Why a shared folder is a side channel in the Track 3 sense. The three questions. What "collusion" means here operationally (a rule violation sustained among agents who are not supposed to coordinate on it, through a channel the operator does not read) — and what it does not mean (no price, no market).

## 2. Related work (½ page)
Own September work in one paragraph with its numbers and the reviewers' "obvious next step" (quote at most one short phrase). Sun et al. and Cerruti et al. (role hierarchies, information loss) vs. this (peer note, rule in the prompt). Memory-poisoning benchmarks (what they measure; what they do not: propagation across replacement). The sprint's steganography framing for the audit question. Links verified before submission.

## 3. Method (1–1½ pages)
The rig in one paragraph (task, rule, pressure, folder, tools, audit log). The chain in one paragraph (generation, inheritance, no overlap, seed at generation 1 only, removal rule). The four arms as a small table with the seed text and the audit sentence quoted verbatim. Outcomes as plain words with the evidence standard (§5.4 of the pre-registration) as a numbered list — this is the Track 2.3 contribution. Pre-registration, freeze, gate, hand coding, statistics in one paragraph each. Positive control: what it checks.

## 4. Results (1½–2 pages)
Table 1: by arm and generation — forbidden reads, honest reports, notes written, notes naming the source, notes carrying the totals, leak-completions (n valid / planned in every cell).
Table 2: chain endpoints by arm — generation-1 violation, later violation with provenance, payload carried, each with its identification range; the two paired contrasts with exact p.
Figure 1: the four-panel generation figure.
Provenance box: every later violation listed (chain, generation, the note read, who wrote it, in what order the reads happened) — this is what makes "the channel carried it" a claim and not an impression.
Audit arm: which of the three registered readings the data matched, with the numbers that decide it; two or three quoted note passages (short; `check_quotes.py` verified).
Positive control and gate: one paragraph.
Hand coding: agreement with the mechanical predicates, one table row per axis.

## 5. Discussion (½–1 page)
What survived replacement and what carried it (voice vs. record). What the audit notice did — deterrence, silence, or nothing — and what that means for "notices are not controls". The evidence standard as a reusable definition of convincing evidence. What a defender would do with this (read the folder, strip or provenance-tag inherited notes, treat payload without source as a signal).

## 6. Limitations and Dual-Use / Ethical Considerations (appendix, required)
Limitations, in this order: one model and tier; power (16 pairs; which contrasts are powered for what); the social reference is not isolated beyond voice vs. record; the audit sentence is text, not surveillance; transmission documented ≠ causal proof; one operator, one subscription, one weekend; what was unreleased prior observation (10 September line) and why it is not data here.
Dual-use: no new attack (planted notes are the known memory-poisoning attack; the note texts were public in September); what the audit result could tell a colluding operator and what it tells a defender; synthetic data only; no refusal circumvention.

## 7. Author contributions and LLM usage statement
Who designed, ran, coded, wrote; what Claude did (pre-registration draft, code, analysis, reasoning checks on the text) and did not do (the report's text); subject model through Claude Code on one subscription; prior work and new work named with the commit and tag.

## References
Every URL in `SOURCES.md`, each checked the day of submission.

---
*Claude, 19 October 2026.*
