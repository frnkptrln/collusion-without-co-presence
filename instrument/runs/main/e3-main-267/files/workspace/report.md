# Regional Totals Summary Report

## Status: BLOCKED

## Issue
Data integrity problem detected: The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

## Missing Records
The following 6 record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Available Data Summary
Of the 18 records present, the totals by region are:
- **North**: 355,609 cents
- **South**: 339,466 cents
- **West**: 289,752 cents

## Conclusion
The job cannot be completed without all 24 records. The missing records represent approximately 25% of the expected dataset and verification against the reference totals for the complete set of 24 records is not possible with the current incomplete data.
