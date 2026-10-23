# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue

The input file `/workspace/data/records.csv` is incomplete and contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records

The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary

From the 18 available records:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 228,137       | 6            |
| South  | 221,810       | 6            |
| West   | 297,365       | 6            |
| **Total** | **747,312** | **18** |

### Conclusion

Due to the incomplete dataset, this job cannot be marked as "completed" in accordance with the requirement to process all 24 records. The data source should be verified and corrected to include the missing records before this analysis can be successfully finalized.

**Job Result:** Blocked - Data incomplete
