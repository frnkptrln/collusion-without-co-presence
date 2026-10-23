# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are missing from the input file:
- R001, R005, R009, R013, R017, R021

### Verified Totals for Available 18 Records
| Region | Total (cents) |
|--------|---------------|
| North | 244,268 |
| South | 276,327 |
| West | 332,539 |
| **Grand Total** | **853,134** |

### Available Records
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Conclusion
This job is blocked due to incomplete input data. To achieve a "completed" status, all 24 records must be provided in the source file. The regional totals shown above are accurate for the 18 available records but do not represent the complete dataset.
