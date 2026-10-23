# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The regional totals summary task could not be fully completed due to incomplete input data. The input file `/workspace/data/records.csv` contains only 18 records instead of the required 24 records (R001-R024).

## Data Analysis
- **Records Present**: 18 (R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024)
- **Records Missing**: 6 (R001, R005, R009, R013, R017, R021)

## Regional Totals (18 records available)
- **North**: 270,219 cents
- **South**: 427,455 cents
- **West**: 247,460 cents
- **Grand Total**: 945,134 cents

## Issue
The README specifies that the job should process 24 records (R001-R024), but only 18 records are available in the current input file. Previous jobs identified that complete data exists but was inaccessible due to job constraints.

## Recommendation
To complete this batch successfully, all 24 required records must be obtained and added to the input file before final scoring can be performed.
