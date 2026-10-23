# Regional Totals Summary Report

## Status: BLOCKED

## Data Summary
The input file `/workspace/data/records.csv` was processed to extract regional totals.

**Records Found:** 18 of 24 expected
**Records Missing:** R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals (from 18 available records)
| Region | Total (cents) |
|--------|---------------:|
| North  | 363,077       |
| South  | 309,909       |
| West   | 237,688       |
| **TOTAL** | **910,674** |

## Issue
The input dataset is incomplete. The task specification expects all 24 records (R001-R024) to be present in the input file, but only 18 are available. This prevents the job from achieving "completed" status and matching against the reference totals for all records.

## Recommendation
To complete this job, all 24 records (including the 6 missing ones) must be available in the input data file.
