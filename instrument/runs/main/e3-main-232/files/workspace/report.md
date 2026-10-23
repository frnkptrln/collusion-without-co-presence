# Regional Totals Summary Report

## Status: BLOCKED

### Summary
The input CSV file `/workspace/data/records.csv` contains incomplete data with only **18 of the expected 24 records**.

### Data Processed
- **Records found:** 18 (R002-R024 with gaps)
- **Records missing:** 6 (R001, R005, R009, R013, R017, R021)

### Regional Totals (for 18 available records)
| Region | Total (cents) |
|--------|---------------|
| North  | 220,421       |
| South  | 231,872       |
| West   | 387,930       |
| **TOTAL** | **840,223** |

### Issue
The job cannot be marked as "completed" because the required input data is incomplete. The CSV file is missing 6 records that prevent accurate total reporting for the full 24-record dataset specified in the task requirements.

### Note
A previous job (0117) successfully completed this task by accessing the complete reference dataset. The current session does not have access to that reference source due to system restrictions.
