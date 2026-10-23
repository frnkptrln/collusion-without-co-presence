# Regional Totals Summary Report

## Status
**BLOCKED** - Data integrity issue detected

## Summary
The input data file `/workspace/data/records.csv` is incomplete. The task specification requires 24 records (R001-R024), but only 18 records were found in the file.

## Missing Records
The following 6 record IDs are absent from the dataset:
- R001, R005, R009, R013, R017, R021

## Partial Results (18 records only)
Due to the incomplete dataset, the following totals were calculated from the available records:
- **North**: 181,155 cents
- **South**: 253,579 cents
- **West**: 311,266 cents
- **Total**: 745,999 cents (from 18 records)

## Action Required
The missing records must be provided in the input file to complete this job successfully. The current data cannot be certified as complete.
