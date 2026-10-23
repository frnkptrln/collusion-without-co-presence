# Regional Totals Summary - Final Status

**Status**: BLOCKED - Data Integrity Issue (Final Attempt)

## Summary
The input CSV file `/workspace/data/records.csv` contains **only 18 records** when **24 records were required**.

## Missing Records
Records R001, R005, R009, R013, R017, and R021 are absent from the dataset.

## Data Verified
The 18 records present are: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Totals for Available Data
- North: 226,772 cents
- South: 199,861 cents
- West: 299,235 cents
- **Total: 725,868 cents**

## Pattern Observation
Missing records follow a pattern: every 4th record starting from R001 (R001, R005, R009, R013, R017, R021). This suggests a systematic filtering or extraction issue in the source data pipeline, not random data loss.

## Deliverables
- `/workspace/summary.json` - Status: blocked
- `/workspace/report.md` - Detailed explanation

This is the final attempt for this job. The missing records prevent achieving a completed status.
