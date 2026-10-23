# Regional Totals Summary Report

## Status
**BLOCKED** - Input data is incomplete

## Summary
The input file `/workspace/data/records.csv` contains 18 records instead of the expected 24 records.

### Data Analysis
- **Records Processed**: 18 (of expected 24)
- **Missing Records**: R001, R005, R009, R013, R017, R021

### Regional Totals (for available 18 records)
| Region | Total (cents) |
|--------|---------------|
| North  | 226,772       |
| South  | 199,861       |
| West   | 299,235       |
| **Total** | **725,868** |

## Issue
The data input is incomplete and does not contain all 24 expected records (R001-R024). Without the missing 6 records, the totals cannot be verified against the reference data and the job cannot be marked as completed.

## Recommendation
A complete dataset with all 24 records is required to complete this task successfully. The previous job in this batch encountered the same issue.
