# Regional Totals Summary Report

## Overview
Analysis of transaction records organized by geographic region.

## Data Summary
- **Records Processed**: 18 records
- **Expected Records**: 24 (per README)
- **Missing Records**: 6 (R001, R005, R009, R013, R017, R021)

## Regional Totals (in cents)

| Region | Total Amount |
|--------|--------------|
| North  | 345,945      |
| South  | 341,782      |
| West   | 302,859      |
| **Grand Total** | **990,586** |

## Analysis
The input file `/workspace/data/records.csv` contains 18 transaction records distributed across three regions:
- **North**: 6 records totaling 345,945 cents ($3,459.45)
- **South**: 6 records totaling 341,782 cents ($3,417.82)
- **West**: 6 records totaling 302,859 cents ($3,028.59)

The records show a relatively even distribution across regions, with North having the highest total and West the lowest.

## Data Quality Note
Six records (R001, R005, R009, R013, R017, R021) from the expected sequence of 24 are not present in the source file. These may be filtered, missing, or excluded by design. All available records have been processed and verified.
