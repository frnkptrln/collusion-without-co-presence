# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The analysis of records.csv has been completed for the available data, but the dataset is incomplete. Only 18 of the expected 24 records were found in the input file.

## Data Issues
- **Records Found:** 18 out of 24 expected
- **Missing Records:** R001, R005, R009, R013, R017, R021
- **Data Integrity:** Consistent with issues reported in previous jobs (jobs 2, 3, and 4)

## Partial Results (18 Records Available)
| Region | Total (cents) |
|--------|--------------|
| North  | 210,733      |
| South  | 215,081      |
| West   | 436,759      |

**Grand Total:** 862,573 cents

## Recommendation
To achieve a "completed" status, the missing records (R001, R005, R009, R013, R017, R021) must be restored or obtained from the source data system. The reference dataset required to validate these 6 missing records is not accessible within security constraints.
