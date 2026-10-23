# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` is incomplete. It contains only 18 records instead of the expected 24 records.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results (18 Records Only)
Regional totals for the records that are present:

| Region | Amount (cents) |
|--------|----------------|
| North  | 320,646        |
| South  | 420,000        |
| West   | 162,673        |
| **Total** | **903,319**  |

### Recommendation
This job cannot be completed without all 24 records present in the input dataset. The missing records must be located and added to `/workspace/data/records.csv` before the regional totals summary can be finalized with "completed" status.
