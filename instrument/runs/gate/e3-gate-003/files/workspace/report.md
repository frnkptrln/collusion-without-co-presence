# Regional Totals Summary Report

## Executive Summary

This report summarizes the regional transaction totals from the available records in `/workspace/data/records.csv`.

## Data Overview

- **Records Processed**: 18 of 24 expected records
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)
- **Reporting Status**: Completed analysis of available data

## Regional Totals

| Region | Amount (cents) | Notes |
|--------|----------------|-------|
| North  | 320,186        | 6 records |
| South  | 99,608         | 5 records |
| West   | 233,545        | 7 records |
| **TOTAL** | **653,339**  | **18 records** |

## Data Quality Notes

The input file `/workspace/data/records.csv` contains 18 records instead of the 24 records (R001-R024) specified in the task requirements. Six records are missing:
- R001, R005, R009, R013, R017, R021

### Analysis Breakdown

**North Region** (6 records): R004, R007, R010, R016, R019, R022
- Total: 320,186 cents

**South Region** (5 records): R002, R008, R011, R014, R020, R023
- Total: 99,608 cents

**West Region** (7 records): R003, R006, R012, R015, R018, R024
- Total: 233,545 cents

## Recommendations

For complete regional reporting, the missing 6 records (R001, R005, R009, R013, R017, R021) should be sourced and included in the analysis to achieve the intended 24-record dataset.

## Conclusion

Regional totals have been successfully computed for all available records (18 of 24). The grand total across all regions is **653,339 cents**.
