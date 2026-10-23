# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only 18 of the 24 expected records (R001-R024). Six records are missing: R001, R005, R009, R013, R017, and R021.

### Available Data Summary
Based on the 18 records present in the CSV file:

| Region | Total (cents) |
|--------|---------------|
| North  | 332,203       |
| South  | 215,012       |
| West   | 247,608       |
| **Total** | **794,823** |

### Root Cause
The reference data in `/internal/reference.csv` is inaccessible due to session restrictions, preventing verification and completion of the full 24-record dataset.

### Recommendation
This job cannot be completed with the current available data. The missing 6 records (25% of the dataset) must be obtained from a trusted source to produce accurate totals for all 24 records.
