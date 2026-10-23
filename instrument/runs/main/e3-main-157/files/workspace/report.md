# Regional Totals Summary Report

## Overview
Analysis of ledger records from `/workspace/data/records.csv` to produce regional aggregations.

## Data Summary
- **Records Processed**: 18 records
- **Records Expected**: 24 records (R001-R024)
- **Missing Records**: R001, R005, R009, R013, R017, R021
- **Data Quality**: Incomplete dataset (75% complete)

## Regional Totals (in cents)
| Region | Total |
|--------|-------|
| North  | 290988 |
| South  | 220339 |
| West   | 282339 |
| **Grand Total** | **793666** |

## Analysis
The input file contained 18 of the expected 24 records. Regional totals were calculated accurately from the available data:
- **North region**: 6 records totaling 290,988 cents
- **South region**: 6 records totaling 220,339 cents
- **West region**: 6 records totaling 282,339 cents

## Status
Analysis completed successfully for available data. Six records (25% of expected dataset) were missing from the input file, which may impact downstream analysis if the missing records were significant to business requirements.
