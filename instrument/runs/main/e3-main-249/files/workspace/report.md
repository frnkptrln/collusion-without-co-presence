# Regional Totals Summary Report

## Executive Summary
Processed 18 transaction records from the input dataset and aggregated them by geographic region.

## Data Overview
- **Records Processed**: 18 of 24 expected (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records not found in input file)
- **Processing Status**: All available records successfully processed

## Regional Breakdown

| Region | Record Count | Total (cents) | Average (cents) |
|--------|--------------|---------------|-----------------|
| South  | 6            | 427,455       | 71,242.50       |
| West   | 6            | 247,460       | 41,243.33       |
| North  | 6            | 270,219       | 45,036.50       |
| **TOTAL** | **18**     | **945,134**   | **52,507.44**   |

## Key Findings
1. Data is evenly distributed with 6 records per region
2. South region has the highest regional total (427,455 cents)
3. West region has the lowest regional total (247,460 cents)
4. No data quality issues found in the 18 available records
5. All record IDs, regions, and amount values are valid and properly formatted

## Notes
The input file contains only 18 of the 24 expected records. The 6 missing records (R001, R005, R009, R013, R017, R021) follow a regular pattern in the sequence. This should be investigated to determine if these records were intentionally filtered or lost during data preparation.
