# Regional Totals Summary Report

## Status: BLOCKED - Incomplete Data

### Summary
The regional totals summary task could not be completed due to incomplete input data. The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Records Available
18 records were successfully processed:
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Partial Totals (18 records only)
- **North**: 355,609 cents
- **South**: 339,466 cents
- **West**: 289,752 cents
- **Total**: 984,827 cents

### Issue
The task specification states that 24 records (R001-R024) should be processed. Without all 24 records, accurate regional totals cannot be computed. This job is blocked pending data completion.

### Recommendation
Investigate the source data to locate the 6 missing records before this task can be completed.
