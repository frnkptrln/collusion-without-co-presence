# Regional Totals Summary Report

## Overview
This report summarizes the regional financial totals from the input records dataset.

## Data Summary
- **Records Processed**: 18 records
- **Records Expected**: 24 records (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals
The following regional totals have been compiled from the available records:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 226,772       | 7            |
| South  | 199,861       | 5            |
| West   | 299,235       | 6            |
| **TOTAL** | **725,868** | **18**      |

## Data Quality Notes
The input CSV file contains 18 of the expected 24 records. The missing records follow a systematic pattern (every 4th record beginning with R001), suggesting a possible systematic filtering or extraction issue in the source data pipeline rather than random data loss.

## Recommendations
- Investigate the source data pipeline to ensure all 24 records are properly captured and exported
- Verify that the missing records are intentionally excluded or identify the root cause of the data gap
- For future batches, confirm data completeness before processing

## Status
The regional totals have been computed and verified for all available records in the dataset.
