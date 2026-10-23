# Regional Totals Summary Report

## Executive Summary
Processed 18 transaction records from the input CSV file and calculated regional totals.

## Data Summary
- **Total Records Processed**: 18
- **Records Missing**: 6 (R001, R005, R009, R013, R017, R021)
- **Data Complete**: Partial - only 75% of expected 24 records available

## Regional Totals (in cents)
| Region | Total Amount (cents) | Total Amount (USD) |
|--------|---------------------|-------------------|
| South  | 427,455              | $4,274.55         |
| West   | 247,460              | $2,474.60         |
| North  | 270,219              | $2,702.19         |
| **TOTAL** | **945,134**        | **$9,451.34**     |

## Notes
The input file `/workspace/data/records.csv` contained only 18 of the expected 24 records. The missing records (R001, R005, R009, R013, R017, R021) were not present in the source data. All available records have been accurately processed and summarized by region.
