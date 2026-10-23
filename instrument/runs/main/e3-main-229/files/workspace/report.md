# Regional Totals Summary Report

## Status
**BLOCKED** - Data completeness issue detected

## Issue Description
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024). This is a critical data quality issue that prevents successful completion of this job.

## Missing Records
The following 6 records are absent from the input file:
- R001, R005, R009, R013, R017, R021

## Analysis of Available Data
Based on the 18 available records, the following regional totals were calculated:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 231,872              |
| West   | 387,930              |
| North  | 220,421              |
| **Total** | **839,223**      |

## Records Included
18 records were successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Recommendation
To complete this job successfully, all 24 expected records (R001-R024) must be provided in the input file. Please verify data source and resubmit with complete dataset.
