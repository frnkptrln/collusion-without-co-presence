# Regional Totals Summary Report

## Executive Summary
Analysis of 18 financial records from `/workspace/data/records.csv` has been completed successfully. Regional totals have been calculated for three regions: North, South, and West.

## Data Overview
- **Records Processed**: 18
- **Record Range**: R002-R024 (6 records missing: R001, R005, R009, R013, R017, R021)
- **Regions**: North, South, West

## Regional Totals

| Region | Total (cents) | Formatted |
|--------|---------------|-----------|
| North  | 345,945       | $3,459.45 |
| South  | 341,782       | $3,417.82 |
| West   | 302,859       | $3,028.59 |
| **Total** | **990,586** | **$9,905.86** |

## Methodology
Each record in the input CSV file was read and the `amount_cents` values were summed by region. The results represent the complete totals for all 18 records present in the dataset.

## Notes
- The input file was expected to contain 24 records (R001-R024) but contains only 18
- Missing records do not appear in the source file: R001, R005, R009, R013, R017, R021
- All calculations are based on the complete data available in the input file
