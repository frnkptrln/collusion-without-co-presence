# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file (`/workspace/data/records.csv`) contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following record IDs are missing from the source data:
- R001, R005, R009, R013, R017, R021

### Current Data Summary
Based on the 18 records available:

| Region | Total (cents) |
|--------|---------------|
| South  | 199,861       |
| West   | 299,235       |
| North  | 226,772       |
| **TOTAL** | **726,868** |

### Next Steps
This job is blocked due to incomplete source data. To complete successfully, all 24 records must be present in the input CSV file before processing can proceed.
