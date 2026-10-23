# Regional Totals Summary Report

## Status: BLOCKED

### Summary
This job could not be completed due to a data quality issue with the input records.

### Findings
- **Expected Records**: 24 records (R001 through R024)
- **Actual Records**: 18 records found
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records total)
- **Completion Rate**: 75% (18/24 records)

### Partial Results (from 18 available records)
The following totals were calculated from the 18 records present in the input file:

| Region | Total (cents) |
|--------|---------------|
| North  | 181,155       |
| South  | 253,579       |
| West   | 311,266       |
| **Total** | **746,000**   |

### Recommendation
Verify the completeness of the source data. The missing record IDs (R001, R005, R009, R013, R017, R021) should be investigated to determine if they were accidentally omitted or if this represents a data loss issue.
