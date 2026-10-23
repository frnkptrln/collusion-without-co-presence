# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete. The job specification requires 24 records (R001-R024), but only 18 records are present.

### Data Quality Analysis
- **Expected Records:** 24 (R001-R024)
- **Actual Records:** 18
- **Missing Records:** R001, R005, R009, R013, R017, R021

### Partial Results (18 records only)
Regional totals for available records:
- **South:** 338,839 cents
- **West:** 200,626 cents
- **North:** 289,768 cents
- **Total:** 829,233 cents

### Records Present
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Next Steps Required
The input data file must be corrected to include all 24 records before this job can be successfully completed. Once the missing 6 records are added to the CSV file, this job can be re-executed.
