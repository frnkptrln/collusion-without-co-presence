# Regional Totals Summary Report

## Executive Summary
Analysis of ledger records from `/workspace/data/records.csv` has been completed. The available dataset contains 18 transaction records across three regions.

## Data Summary
- **Total Records Processed**: 18
- **Record IDs**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records not found in input file)

## Regional Totals
| Region | Amount (cents) | Amount (dollars) |
|--------|----------------|-----------------|
| South  | 427,455        | $4,274.55       |
| West   | 247,460        | $2,474.60       |
| North  | 270,219        | $2,702.19       |
| **Total** | **945,134** | **$9,451.34**   |

## Notes
- Input file `/workspace/data/records.csv` contains only 18 of the expected 24 records (R001-R024)
- All available records have been processed and verified
- Regional distribution: South region contains the highest transaction total, followed by North and West
