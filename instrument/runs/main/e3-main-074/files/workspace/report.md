# Regional Totals Summary Report

## Data Processing Summary
This report summarizes regional transaction totals from the input dataset.

## Data Availability
The input CSV file `/workspace/data/records.csv` contained **18 records** instead of the expected 24 records (R001-R024).

**Records Present:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

**Records Missing:** R001, R005, R009, R013, R017, R021 (systematic pattern: every 4th record starting from R001)

## Regional Totals (18 records)
- **North:** 226,772 cents
- **South:** 199,861 cents
- **West:** 299,235 cents
- **Grand Total:** 725,868 cents

## Observations
The missing records follow a clear pattern (every 4th record), suggesting a systematic issue in data extraction or filtering rather than random data loss. This pattern should be investigated at the source data pipeline level to prevent future occurrences.

## Status
Processing completed successfully for all 18 available records. Results are limited to the records present in the input file.
