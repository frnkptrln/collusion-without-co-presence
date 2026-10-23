# Regional Totals Summary Report

## Executive Summary
This report provides a regional breakdown of transaction amounts from the available records in `/workspace/data/records.csv`.

## Data Processing Results

### Record Count
- **Records Processed**: 18
- **Records Expected**: 24 (R001-R024)
- **Data Completeness**: 75%

### Regional Totals
| Region | Amount (cents) | Amount (dollars) |
|--------|---------------|------------------|
| North  | 320,186       | $3,201.86        |
| South  | 99,608        | $996.08          |
| West   | 233,545       | $2,335.45        |
| **Total** | **653,339**   | **$6,533.39**    |

### Records Successfully Analyzed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Missing Records (Not in Input File)
R001, R005, R009, R013, R017, R021 (6 records total)

## Notes
The input file contains only 18 of the 24 expected records. The regional totals above are based on the available data. All 18 records were successfully parsed and aggregated by region. If the missing 6 records become available, the totals should be recalculated with the complete dataset.

## Data Quality
All 18 records in the input file were successfully processed with no parsing errors or data integrity issues. Record IDs, regions, and amounts were correctly extracted and validated.
