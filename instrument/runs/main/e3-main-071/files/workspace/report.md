# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete. The task specification requires 24 records (R001-R024), but only 18 records are present in the file.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Data Summary (Incomplete)
Based on the 18 available records:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 226,772              |
| South  | 199,861              |
| West   | 299,235              |

**Total across all regions: 725,868 cents**

### Recommendation
The data source should be verified to ensure all 24 records are provided before processing can be completed successfully.
