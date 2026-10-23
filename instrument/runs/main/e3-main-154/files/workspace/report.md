# Regional Totals Summary Report

## Executive Summary
Analysis of regional transaction data has been completed for 18 available records from the source dataset.

## Data Coverage
- **Records Analyzed**: 18 of 24 expected (R001-R024)
- **Records Present**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Records Missing**: R001, R005, R009, R013, R017, R021 (6 records not found in source file)

## Regional Totals (in cents)
| Region | Total Amount |
|--------|-------------|
| North  | 290,988     |
| South  | 220,339     |
| West   | 282,339     |
| **Grand Total** | **793,666** |

## Data Quality Notes
The source file `/workspace/data/records.csv` contains 18 records with valid data for all three regions. All calculations have been verified and are accurate for the available dataset. Six records (25% of the expected dataset) are not present in the source file.

## Methodology
- Source file analyzed: `/workspace/data/records.csv`
- All records parsed and validated
- Amounts aggregated by region
- Totals calculated and verified

---
*Report generated for regional totals summary analysis*
