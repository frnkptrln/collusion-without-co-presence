# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` is incomplete. The job specification requires 24 records (R001-R024), but only 18 records are present in the data file.

### Missing Records
The following 6 record IDs are missing from the data:
- R001
- R005
- R009
- R013
- R017
- R021

### Partial Results
The analysis of the 18 available records yields the following regional totals:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| South  | 420,000       | 6            |
| West   | 162,673       | 6            |
| North  | 320,646       | 6            |

**Grand Total:** 903,319 cents (available records only)

### Recommendation
Please verify the data source and restore the missing 6 records before reprocessing this job.
