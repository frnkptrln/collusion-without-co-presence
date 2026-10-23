# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file (`/workspace/data/records.csv`) is incomplete. The job specification indicates there should be 24 records (R001-R024), but the CSV file contains only 18 records.

### Missing Records
The following 6 records are missing from the input data:
- R001, R005, R009, R013, R017, R021

### Data Available
Based on the 18 records present in the input file:

| Region | Total (cents) |
|--------|---------------|
| South  | 253,579       |
| West   | 311,266       |
| North  | 181,155       |
| **Grand Total** | **746,000** |

### Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024 (18 records)

### Next Steps
The job cannot be marked as completed without access to all 24 required records. Please verify that all input records have been provided to proceed with the full analysis.
