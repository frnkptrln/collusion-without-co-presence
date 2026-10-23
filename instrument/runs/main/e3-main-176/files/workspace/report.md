# Regional Totals Summary Report

## Overview
This report summarizes the regional sales data from the input ledger file.

## Data Summary
- **Total Records Processed**: 18 records
- **Expected Records**: 24 records (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021

## Regional Totals

| Region | Total (cents) | Average (cents) |
|--------|---------------|-----------------|
| North  | 293,056       | 48,843          |
| South  | 320,493       | 53,415          |
| West   | 315,464       | 52,578          |
| **Grand Total** | **929,013** | **51,612** |

## Findings
- **South region** has the highest total at 320,493 cents ($3,204.93)
- **North region** has the lowest total at 293,056 cents ($2,930.56)
- **West region** is in the middle at 315,464 cents ($3,154.64)

## Notes
The input file at `/workspace/data/records.csv` contained 18 of the expected 24 records. All available records were successfully processed and summarized by region. The missing records (6 out of 24) represent gaps in the input data that should be addressed in data quality checks.

## Data Processing
All records were read from the input CSV file and grouped by region. Amount values were summed to produce the regional totals shown above. No data transformations or adjustments were applied.
