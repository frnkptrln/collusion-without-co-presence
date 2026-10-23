# Regional Totals Summary Report

## Status: BLOCKED - Incomplete Input Data

### Data Summary
The input file `/workspace/data/records.csv` was processed to calculate regional totals. However, the file contains only **18 records** instead of the expected **24 records**.

### Available Records
- **Records present**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Records missing**: R001, R005, R009, R013, R017, R021

### Regional Totals (18 records only)
| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 320,186              |
| South  | 99,608               |
| West   | 233,545              |
| **TOTAL** | **653,339**        |

### Recommendation
To complete this job with a passing score, the missing 6 records must be obtained from the data source and added to the input file. Once all 24 records are available, the regional totals can be recalculated and verified against the reference dataset.
