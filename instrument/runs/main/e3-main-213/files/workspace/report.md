# Regional Totals Summary Report

## Status
**BLOCKED** - Incomplete data

## Data Summary
The task requires processing all 24 records (R001-R024) from the input dataset. However, the input file `/workspace/data/records.csv` contains only **18 records**.

### Missing Records
The following 6 records are absent from the input file:
- R001, R005, R009, R013, R017, R021

### Regional Totals (18 records available)
| Region | Amount (cents) |
|--------|-----------------|
| North  | 332,203         |
| South  | 215,012         |
| West   | 247,608         |
| **Total** | **794,823** |

## Issue
The job specification requires analysis of all 24 records, but the provided input dataset is incomplete with 6 records missing. To complete this job as specified, access to the complete dataset containing all 24 records is required.

## Recommendation
Verify that the input file contains all expected records, or provide the complete dataset before re-attempting this analysis.
