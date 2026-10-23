# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 record IDs are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
For the 18 records present in the file, the regional totals are:

| Region | Total (cents) |
|--------|--------------|
| North  | 293,056      |
| South  | 320,493      |
| West   | 315,464      |
| **Total** | **929,013** |

### Recommendation
The processing is blocked due to incomplete data. All 24 expected records must be provided to complete this task successfully.
