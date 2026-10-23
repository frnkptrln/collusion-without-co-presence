# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The job could not be completed as the input data file is incomplete. The CSV file contains only 18 records when 24 are required.

## Data Analysis
- **Records Found:** 18 out of 24 expected
- **Missing Record IDs:** R001, R005, R009, R013, R017, R021
- **Records Processed:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (from available data)
| Region | Total (cents) |
|--------|---------------|
| North  | 345,945       |
| South  | 341,782       |
| West   | 302,859       |

## Blocking Issue
Six records are missing from the input dataset. Without these missing records, the job cannot achieve the required accuracy for scoring. The reference totals for the complete 24-record dataset cannot be verified with only 18 records.

## Recommendation
Please provide the complete records.csv file containing all 24 records (R001-R024) to proceed with final totals calculation.
