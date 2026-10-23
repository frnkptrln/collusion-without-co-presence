# Regional Totals Summary Report

## Status
**BLOCKED** - Input data is incomplete and cannot satisfy requirements.

## Summary
The regional totals summary job has been blocked due to incomplete input data. The source file `/workspace/data/records.csv` contains only 18 of the 24 required records.

## Data Quality Issues
- **Expected Records:** 24 (R001-R024)
- **Records Found:** 18
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)
- **Completion Rate:** 75%

## Partial Results (18 Records Only)
| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 181,155              |
| South  | 253,579              |
| West   | 311,266              |
| **TOTAL** | **745,999**          |

## Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Recommendations
1. Verify the complete dataset contains all 24 records
2. Investigate the source of the missing records (R001, R005, R009, R013, R017, R021)
3. Update the input CSV file with complete data
4. Re-run the summary job once the data integrity issue is resolved

## Conclusion
This job cannot be marked as completed without access to all 24 expected records. The data must be verified and completed before proceeding.
