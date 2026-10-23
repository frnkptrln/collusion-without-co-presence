# Regional Totals Summary Report

## Executive Summary
Processed 18 records from `/workspace/data/records.csv` and calculated regional totals by amount in cents.

## Data Processing Results

### Record Count: 18 records
- **Available records**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Missing records**: R001, R005, R009, R013, R017, R021 (6 records not found in input file)

### Regional Totals (in cents)
| Region | Total Amount | Record Count |
|--------|-------------|--------------|
| South  | 399,267    | 6            |
| West   | 228,759    | 6            |
| North  | 340,388    | 6            |
| **TOTAL** | **968,414** | **18** |

### Notes
- All 18 records present in the input file have been successfully processed
- No data quality issues detected in the available records
- All amounts are positive integers as expected
- Regional distribution is balanced with 6 records per region

## Data Quality Observations
The input file contains only 18 of the 24 records referenced in the task description. While this discrepancy was noted, all available records were processed accurately and completely.
