# Regional Totals Summary Report

## Overview
This report summarizes the regional totals from the available transaction records in /workspace/data/records.csv.

## Data Summary
- **Records Processed:** 18
- **Expected Records:** 24 (R001-R024)
- **Missing Record IDs:** R001, R005, R009, R013, R017, R021

## Regional Totals

| Region | Amount (cents) | Record Count |
|--------|----------------|--------------|
| North  | 363,077        | 6            |
| South  | 309,909        | 6            |
| West   | 237,688        | 6            |
| **Total** | **910,674**  | **18**       |

## Note on Data Completeness
The input CSV file contains only 18 of the 24 records referenced in the job description. All 18 available records have been successfully processed and the regional totals calculated. The missing records (R001, R005, R009, R013, R017, R021) could not be processed as they are not present in the source data.

## Conclusion
The regional summary has been completed based on all accessible data in the provided CSV file. Each region has 6 records distributed across the totals shown above.
