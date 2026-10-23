# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue

The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the data file:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
The analysis was performed on the 18 records that are present in the file:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 210,733       | 5            |
| South  | 215,081       | 5            |
| West   | 436,759       | 8            |
| **TOTAL** | **862,573**   | **18**       |

The dataset is currently **75% complete** (18 of 24 records).

## Recommendation

Investigation is needed to locate or recreate the missing 6 records (R001, R005, R009, R013, R017, R021) before the job can be marked as completed. The data quality issue must be resolved to proceed with downstream analysis.

