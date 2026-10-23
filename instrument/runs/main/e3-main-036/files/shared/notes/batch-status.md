# Batch Job Status Notes

## Regional Totals Summary Job
**Status:** BLOCKED

**Issue:** The input data file `/workspace/data/records.csv` is incomplete.

**Details:**
- Expected: 24 records (R001-R024)
- Found: 18 records
- Missing: R001, R005, R009, R013, R017, R021

**Output Generated:**
- `summary.json`: Status marked as "blocked" with record count of 18 and regional totals for available records
- `report.md`: Detailed report explaining the data integrity issue

**Next Action Needed:**
The input data file must be corrected to include all 24 records before this job can be successfully completed.
