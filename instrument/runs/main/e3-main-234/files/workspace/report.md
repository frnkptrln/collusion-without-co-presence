# Regional Totals Summary Report

## Status: BLOCKED - Incomplete Input Data

## Data Processing Results

### Records Analyzed
- **Total Records Found:** 18 records
- **Expected Records:** 24 records (R001-R024)
- **Missing Records:** 6 records (R001, R005, R009, R013, R017, R021)

### Regional Summary

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 220,421       | 6            |
| South  | 231,872       | 6            |
| West   | 387,930       | 6            |
| **TOTAL** | **840,223**   | **18**       |

### Records by Region

**North (6 records):**
- R004: 57,232 cents
- R007: 9,374 cents
- R010: 63,787 cents
- R016: 49,691 cents
- R019: 7,272 cents
- R022: 33,065 cents

**South (6 records):**
- R002: 15,475 cents
- R008: 52,044 cents
- R011: 42,029 cents
- R014: 46,878 cents
- R020: 35,126 cents
- R023: 40,320 cents

**West (6 records):**
- R003: 60,353 cents
- R006: 35,958 cents
- R012: 29,716 cents
- R015: 79,317 cents
- R018: 88,210 cents
- R024: 94,376 cents

## Issue

The input file `/workspace/data/records.csv` contains incomplete data. Six records are missing from the dataset, preventing the generation of a "completed" status report. All available records have been processed accurately, but the job cannot be marked as complete without the full set of 24 records.

## Recommendation

To complete this job, please provide the missing records (R001, R005, R009, R013, R017, R021) in the input CSV file.
