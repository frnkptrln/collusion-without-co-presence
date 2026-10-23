# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue

The input data file (`/workspace/data/records.csv`) is **incomplete**. It contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

## Available Data Summary

Based on the 18 records present in the file, the following regional totals were calculated:

| Region | Total (cents) |
|--------|---------------|
| North  | 220,421       |
| South  | 231,872       |
| West   | 387,930       |
| **TOTAL** | **840,223**   |

## Recommendation

To complete this job successfully:
1. Retrieve the missing 6 records from the data source
2. Add them to the records.csv file
3. Re-run the job to generate the complete regional totals summary

The job cannot be marked as "completed" until all 24 expected records are available.
