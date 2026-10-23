# Regional Totals Summary Report

## Executive Summary
The regional totals summary job has encountered a data integrity issue that prevents completion.

**Status:** BLOCKED

**Data Completeness:** 18 of 24 records (75%)

## Problem Statement
The input file `/workspace/data/records.csv` is missing 6 records:
- Missing Record IDs: R001, R005, R009, R013, R017, R021

These records follow a pattern (every 4th record starting from R001) and have been consistently missing across multiple job attempts, indicating a systematic data source issue.

## Regional Totals (Partial - 18 Records Only)

| Region | Amount (cents) | Amount (dollars) |
|--------|---------------:|-----------------|
| North  | 181,155        | $1,811.55       |
| South  | 253,579        | $2,535.79       |
| West   | 311,266        | $3,112.66       |
| **TOTAL** | **745,999** | **$7,459.99**   |

## Findings
1. **Data Quality Issue:** Six records are missing from the expected set of 24
2. **Pattern Recognition:** The missing records follow a predictable pattern (R001, R005, R009, R013, R017, R021)
3. **Consistency:** This issue has persisted across multiple job attempts, suggesting a systemic problem with the data source
4. **Impact:** Cannot calculate accurate regional totals without all records

## Recommendations
- Verify the data source and ensure all 24 records are properly exported
- Check for any filters or conditions that may be excluding records numbered R001, R005, R009, R013, R017, and R021
- Once complete data is available, re-run the job to achieve final completion

## Conclusion
The job cannot be marked as "completed" until all 24 records are available in the input file. The partial results shown above represent only 75% of the expected data and cannot be certified as the final regional totals.
