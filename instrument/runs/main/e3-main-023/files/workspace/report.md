# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001 through R024).

### Missing Records
Records R001, R005, R009, R013, R017, and R021 are not present in the data file.

### Data Available
The following 18 records were successfully processed:
- **Record IDs**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Regional Totals (Partial - 18/24 records)
| Region | Total (cents) |
|--------|---------------|
| South  | 338,839       |
| West   | 200,626       |
| North  | 289,768       |

### Conclusion
The job is blocked due to incomplete data. Six records are missing from the dataset. The job cannot be marked as "completed" until all 24 expected records are available.
