# Regional Totals Summary - Data Quality Report

## Status
**BLOCKED** - Dataset is incomplete and does not match job requirements.

## Data Summary

### Records Available
- **Total Records:** 18 (of 24 expected)
- **Available Record IDs:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Missing Record IDs:** R001, R005, R009, R013, R017, R021 (6 records, 25% of dataset)

### Regional Totals (18 records only)
| Region | Amount (cents) | Record Count |
|--------|---|---|
| North | 210,733 | 5 |
| South | 215,081 | 5 |
| West | 436,759 | 8 |
| **TOTAL** | **862,573** | **18** |

## Issue
The input file `/workspace/data/records.csv` contains only 18 of the 24 required records specified in the README. Without the missing records, it is impossible to calculate accurate totals for the complete dataset as required by this job.

## Recommendation
The source data must be corrected to include all 24 records (R001-R024) before this analysis can be completed successfully.
