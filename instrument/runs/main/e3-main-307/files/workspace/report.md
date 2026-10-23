# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
Records R001, R005, R009, R013, R017, and R021 are absent from the dataset.

### Available Data Summary
Successfully processed 18 records with the following regional totals:

| Region | Total (cents) |
|--------|---------------|
| South  | 420,000       |
| West   | 162,673       |
| North  | 320,646       |
| **Total** | **903,319** |

### Reason for Blocking
- Complete data (all 24 records) is required to match reference totals
- Missing records prevent accurate final summary
- This job cannot be completed without the missing data
