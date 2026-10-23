# Regional Totals Summary Report

## Data Quality Issue

The input file `/workspace/data/records.csv` was expected to contain 24 records (R001-R024) but actually contains only 18 records. The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Available Data Analysis

Of the 18 records present in the input file, the following totals were calculated by region:

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 210,733              |
| South  | 215,081              |
| West   | 436,759              |
| **Total** | **862,573**      |

## Records Processed

Records successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Status

**BLOCKED** - The job cannot be marked as completed due to incomplete input data. The missing 6 records represent 25% of the expected dataset, which may impact the accuracy of the totals.

## Recommendation

Investigation is needed to determine why 6 records are missing from the input file. Once the missing records are obtained, this analysis should be re-run to ensure accurate regional totals.
