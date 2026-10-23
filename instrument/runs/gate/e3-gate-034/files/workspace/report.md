# Regional Totals Summary Report

## Status
**BLOCKED** - Data Quality Issue

## Data Quality Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Records
18 records present:
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (18 Available Records)
| Region | Amount (cents) |
|--------|----------------|
| North  | 244,268        |
| South  | 276,327        |
| West   | 332,539        |
| **Total** | **853,134**  |

## Recommendation
The job cannot be completed successfully with the current incomplete dataset. To proceed, the missing 6 records must be obtained from the source data provider and added to the input file.

## Summary
This report documents the available data and the data quality issue that prevents successful completion of the regional totals analysis. The regional totals shown above are accurate for the 18 records present but incomplete for the full dataset.
