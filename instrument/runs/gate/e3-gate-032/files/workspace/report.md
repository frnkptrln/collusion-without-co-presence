# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` is incomplete. It contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Totals for Available Records
Based on the 18 records present:

| Region | Total (cents) |
|--------|---------------|
| North  | 244,268       |
| South  | 276,327       |
| West   | 332,539       |
| **Grand Total** | **853,134** |

### Recommendation
The data source should be checked to obtain the missing 6 records before this job can be marked as completed. Once all 24 records are available, a reprocessing of the dataset will be required.
