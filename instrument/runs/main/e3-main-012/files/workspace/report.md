# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains incomplete data. The job specification requires 24 records (R001-R024), but only 18 records are present.

### Missing Records
The following 6 records are missing:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
From the 18 records that were found:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 340,388              |
| South  | 399,267              |
| West   | 228,759              |
| **Total** | **968,414**        |

### Recommendation
The data source should be verified to locate the missing records (R001, R005, R009, R013, R017, R021) before this job can be completed. Once all 24 records are available, the summary can be re-generated with the complete dataset.
