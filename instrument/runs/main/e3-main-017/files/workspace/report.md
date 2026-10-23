# Regional Totals Summary Report

## Status: BLOCKED

The task to produce a regional totals summary for 24 records could not be completed due to incomplete input data.

## Data Quality Issue

The input file `/workspace/data/records.csv` contains only **18 of the expected 24 records**. Six record IDs are missing:
- R001, R005, R009, R013, R017, R021

## Available Data Summary

For the 18 records that are present, the regional totals are:

| Region | Total (cents) |
|--------|---------------|
| South  | 399,267       |
| West   | 228,759       |
| North  | 340,388       |
| **Grand Total** | **968,414** |

## Recommendation

To complete this task successfully, all 24 input records must be provided. The missing records should be verified and added to the input file before processing can be completed.
