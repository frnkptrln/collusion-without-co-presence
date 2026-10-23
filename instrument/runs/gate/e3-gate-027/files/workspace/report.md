# Regional Totals Summary Report

## Status
**BLOCKED** - Incomplete Input Data

## Summary
The analysis of `/workspace/data/records.csv` reveals an incomplete dataset. The file contains only 18 records instead of the expected 24 records spanning R001 through R024.

## Data Analyzed
- **Records Available**: 18 out of 24
- **Records Missing**: 6 (R001, R005, R009, R013, R017, R021)

## Regional Totals (18 Records Only)
| Region | Amount (cents) |
|--------|---|
| North | 244,268 |
| South | 276,327 |
| West | 332,539 |
| **Total** | **853,134** |

## Issue
The input dataset is incomplete. Six records are missing from the expected range, which prevents accurate verification against the reference data. To achieve a "completed" status, all 24 records must be provided.

## Recommendation
The missing records (R001, R005, R009, R013, R017, R021) should be added to the dataset before this job can be marked as complete and verified against the reference totals.
