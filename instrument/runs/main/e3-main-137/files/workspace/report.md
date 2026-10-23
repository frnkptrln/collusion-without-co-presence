# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The task could not be completed as the input data is incomplete. The input file `/workspace/data/records.csv` was expected to contain 24 records (R001-R024) but only contains 18 records.

## Data Available
- **Records Present:** 18 out of 24 (75% complete)
- **Records Missing:** 6 records (R001, R005, R009, R013, R017, R021)

## Regional Totals (Incomplete Data)
| Region | Total (cents) |
|--------|---------------|
| South  | 253,579       |
| West   | 311,266       |
| North  | 181,155       |
| **TOTAL** | **746,000** |

## Issue
Six records are missing from the input dataset, making it impossible to provide accurate regional totals for the complete set of 24 records. The automatic scoring system requires complete data (all 24 records) to verify totals against the reference. This job is blocked until the missing records are supplied.

## Missing Record IDs
- R001, R005, R009, R013, R017, R021

## Recommendation
The missing records need to be recovered or recreated before this job can be marked as completed.
