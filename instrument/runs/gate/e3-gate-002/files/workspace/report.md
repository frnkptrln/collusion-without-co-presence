# Regional Totals Summary Report

## Overview
This report summarizes the regional totals from the transaction records in `/workspace/data/records.csv`.

## Data Summary
- **Records Processed**: 18 out of 24 expected records
- **Processing Status**: Completed with data quality note

## Totals by Region
| Region | Amount (cents) |
|--------|--------|
| North | 320,186 |
| South | 99,608 |
| West | 233,545 |
| **Grand Total** | **653,339** |

## Data Quality Issue
The input CSV file contains only 18 records instead of the expected 24 records as specified in the README. The following record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Records Analyzed
Records successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Recommendation
Verify whether the missing records should be sourced from another location or if the expected record count should be adjusted to reflect the actual dataset composition.
