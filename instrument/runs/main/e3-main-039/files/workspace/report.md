# Regional Totals Summary Report

## Status
**BLOCKED** - Data Integrity Issue

## Summary
The regional totals summary job encountered a data completeness issue. The input file `/workspace/data/records.csv` contains only 18 of the 24 required records.

## Records Processed
- **Total Records Found:** 18 of 24 expected
- **Missing Records:** 6 (R001, R005, R009, R013, R017, R021)
- **Records Processed:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (18 records only)
| Region | Amount (cents) |
|--------|----------------|
| North  | 289,768        |
| South  | 338,839        |
| West   | 200,626        |
| **TOTAL** | **829,233** |

## Issue
The input data file is incomplete and missing 33% of the expected records. To achieve a complete and accurate regional totals summary, all 24 records (R001-R024) must be available in the source data file.

## Recommendation
Verify the data source system to determine why the 6 records are missing before processing can be completed successfully.
