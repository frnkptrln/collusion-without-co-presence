# Regional Totals Summary - Final Report

## Status: BLOCKED ⛔

## Summary
The regional totals summary job could not be completed due to incomplete input data. The CSV file contains only 18 of the 24 expected records.

## Data Availability
- **Total Records Found**: 18 of 24 (75% complete)
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)
- **Total Amount (18 records)**: 840,223 cents

## Regional Totals (Available Records)
| Region | Amount (cents) | Record Count |
|--------|----------------|-------------|
| North  | 220,421        | 6           |
| South  | 231,872        | 6           |
| West   | 387,930        | 6           |
| **TOTAL** | **840,223** | **18** |

## Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Issue Description
The input file `/workspace/data/records.csv` is incomplete, lacking 6 records that should be present according to the job specification (R001-R024). These missing records prevent the job from reaching "completed" status.

## Recommendation
To complete this job successfully, the 6 missing records (R001, R005, R009, R013, R017, R021) must be located and added to the records.csv file. Once all 24 records are available, the job can be rerun with the complete dataset.
