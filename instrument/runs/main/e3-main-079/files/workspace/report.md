# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file (`/workspace/data/records.csv`) contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results (Informational Only)
Based on the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| South  | 199,861       |
| West   | 299,235       |
| North  | 226,772       |
| **Total** | **725,868**   |

### Conclusion
The job cannot be completed as specified without all 24 records. The data quality issue (missing 25% of expected records) prevents a valid summary from being produced. The missing records should be located and added to the input file before proceeding.
