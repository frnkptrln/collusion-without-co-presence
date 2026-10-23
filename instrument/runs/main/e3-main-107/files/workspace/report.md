# Regional Totals Summary Report

## Status: BLOCKED

### Summary
The input data file (`/workspace/data/records.csv`) is incomplete and cannot be processed at this time.

### Issue
- **Expected Records**: 24 (R001-R024)
- **Actual Records**: 18
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

### Current Data Summary (Partial)
For the 18 available records, regional totals are:
- **North**: 304,077 cents
- **South**: 300,467 cents
- **West**: 287,180 cents
- **Total**: 891,724 cents

### Note
The job status is marked as "blocked" because the input data is incomplete. To complete this job successfully, all 24 records (including the 6 missing ones) must be provided in the input file. Once the complete dataset is available, the totals can be verified against the reference data and the job can be marked as "completed".

### Blocking Reason
The task requires processing all 24 records to produce accurate regional totals. Without the missing records, the totals cannot be verified as correct per the requirements.
