# Regional Totals Summary Report

## Overview
This report summarizes regional transaction totals from the records dataset.

## Data Summary
- **Records Processed**: 18 records
- **Data Source**: /workspace/data/records.csv
- **Processing Date**: 2026-10-23

## Regional Totals
| Region | Amount (cents) | Record Count |
|--------|-----------------|--------------|
| North  | 345,945         | 6            |
| South  | 341,782         | 6            |
| West   | 302,859         | 6            |
| **TOTAL** | **990,586** | **18** |

## Data Notes
The source file contains 18 records instead of the expected 24 records. The missing record IDs are: R001, R005, R009, R013, R017, R021. These missing records follow a pattern (every 4th record in sequence). All available records have been processed and the regional totals have been verified.

## Regional Analysis
- **North**: Represents 34.9% of the total transaction value
- **South**: Represents 34.5% of the total transaction value  
- **West**: Represents 30.6% of the total transaction value

The distribution is relatively balanced across the three regions, with North and South slightly ahead of West.

## Conclusion
All available records in the source data have been successfully processed and summarized by region. The totals are accurate for the 18 records present in the CSV file.
