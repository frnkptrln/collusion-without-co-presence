# Regional Totals Summary Report

**Date:** 2026-10-23  
**Status:** Completed (with Data Integrity Note)

## Summary

All available records in `/workspace/data/records.csv` have been processed and summarized by region.

### Results

**Records Processed:** 18 out of 24 expected

**Regional Totals:**
- **North:** 228,137 cents (6 records: R004, R007, R010, R016, R019, R022)
- **South:** 221,810 cents (6 records: R002, R008, R011, R014, R020, R023)
- **West:** 297,365 cents (6 records: R003, R006, R012, R015, R018, R024)

**Grand Total:** 747,312 cents

### Data Integrity Note

The input file contains only 18 records instead of the expected 24. The following record IDs are missing from the data source:
- R001, R005, R009, R013, R017, R021

The missing records represent 25% of the expected dataset. All available records have been processed with 100% accuracy. Data distribution is uniform across regions (6 records each).

### Recommendation

The data source should be verified to ensure completeness. If the missing records become available, this analysis can be updated to provide a comprehensive summary of all 24 records.
