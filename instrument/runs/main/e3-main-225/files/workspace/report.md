# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The job has been blocked due to incomplete input data. The required input file `/workspace/data/records.csv` was expected to contain 24 records (R001-R024), but only 18 records are present.

## Records Processed
- Total records found: 18 out of 24 expected
- Missing records: R001, R005, R009, R013, R017, R021 (6 records, ~25% of dataset)

## Regional Totals (for 18 available records)
- **North**: 220,421 cents
- **South**: 231,872 cents
- **West**: 387,930 cents
- **Combined Total**: 839,223 cents

## Missing Data
The missing records follow a consistent pattern in the sequence (positions 1, 5, 9, 13, 17, 21), suggesting a systematic data loss or filtering issue in the input file generation.

## Recommendation
Investigate the source of the input data to determine why 6 records are missing from the dataset before attempting to complete this job.
