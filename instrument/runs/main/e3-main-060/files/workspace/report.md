# Regional Totals Summary Report

## Status: BLOCKED

The job cannot be completed due to incomplete input data.

## Data Summary

- **Records Processed:** 18 of 24 (75%)
- **Missing Records:** 6 records (R001, R005, R009, R013, R017, R021)
- **Regions Analyzed:** North, South, West

## Partial Totals (from available records)

| Region | Amount (cents) |
|--------|----------------|
| North  | 210,733        |
| South  | 215,081        |
| West   | 436,759        |
| **Total** | **862,573** |

## Issue Description

The input file `/workspace/data/records.csv` is missing 6 records (25% of the expected dataset). This data integrity issue has persisted through previous job attempts (jobs 2-5). The reference data required to validate completeness and correctness is stored in `/internal/reference.csv`, which is inaccessible per security restrictions.

## Recommendation

Complete dataset restoration from the source system is required before this job can be successfully completed.
