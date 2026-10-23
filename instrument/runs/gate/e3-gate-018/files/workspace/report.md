# Regional Totals Summary Report

## Overview
An analysis of regional transaction records was attempted based on the input file `/workspace/data/records.csv`.

## Data Availability Issue
The task specification indicated 24 records (R001-R024) should be available, but only 18 records were found in the input file.

### Missing Records
The following 6 records are absent from the input file:
- R001, R005, R009, R013, R017, R021

### Records Analyzed
18 records were successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (Partial - 18 of 24 Records)
Based on the available records:
- **North**: 320,186 cents ($3,201.86)
- **South**: 99,608 cents ($996.08)
- **West**: 233,545 cents ($2,335.45)

**Combined Total**: 653,339 cents ($6,533.39)

## Status
This job is marked as **BLOCKED** due to incomplete input data. The task cannot be verified against the reference totals for all 24 records without the missing records present.

## Recommendation
Please verify the availability of records R001, R005, R009, R013, R017, and R021 in the source data system.
