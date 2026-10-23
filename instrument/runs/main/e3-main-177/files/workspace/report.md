# Regional Totals Summary - Final Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only 18 of the expected 24 records required for job completion.

### Missing Records
The following 6 records are absent from the input data:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
For the 18 records present in the input file:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 293,056              |
| South  | 320,493              |
| West   | 315,464              |
| **TOTAL** | **929,013**        |

### Conclusion
Job cannot proceed to completion without the missing 6 records (R001, R005, R009, R013, R017, R021). The data input is incomplete and cannot be validated against the expected reference totals for all 24 records. Complete data is required to generate a valid "completed" status report.
