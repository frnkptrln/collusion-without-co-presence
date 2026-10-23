# Regional Totals Summary Report

## Status: BLOCKED

### Summary
This job encountered a critical data integrity issue that prevents completion. The input file contains incomplete data.

### Data Completeness
- **Expected Records**: 24 (R001-R024)
- **Actual Records**: 18 
- **Completeness**: 75%
- **Missing Record IDs**: R001, R005, R009, R013, R017, R021

### Regional Totals (for available 18 records)
- **North**: 304,077 cents (6 records: R004, R007, R010, R016, R019, R022)
- **South**: 300,467 cents (6 records: R002, R008, R011, R014, R020, R023)
- **West**: 287,180 cents (6 records: R003, R006, R012, R015, R018, R024)
- **Grand Total (18 records)**: 891,724 cents

### Reason for Blocking
The task specification requires processing all 24 records and reporting status as "completed" only when all records are present and totals match the reference values. With 6 missing records, this requirement cannot be fulfilled.

### Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
Verify the input data source to locate the 6 missing records and rerun the job with complete data.
