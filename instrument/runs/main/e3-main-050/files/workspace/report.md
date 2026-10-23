# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains **only 18 records instead of the expected 24 records** specified in the job requirements.

### Missing Records
Six records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

**Pattern:** The missing records follow a systematic pattern (every 4th record starting from record 1), which suggests a systematic issue in data extraction, collection, or filtering rather than random data loss.

### Available Data
**Records Processed:** 18 of 24 (75% coverage)

**Totals by Region:**
- **North:** 210,733 cents (5 records: R004, R007, R010, R016, R019, R022)
- **South:** 215,081 cents (5 records: R002, R008, R011, R014, R020, R023)
- **West:** 436,759 cents (8 records: R003, R006, R012, R015, R018, R024)

**Grand Total:** 862,573 cents

### Impact
The job cannot be marked as "completed" because the dataset is incomplete. The 6 missing records represent 25% of the expected data volume and prevent accurate regional totals calculation.

### Recommendation
Investigate the source data to obtain the 6 missing records before proceeding with downstream analysis. The systematic pattern of missing records suggests the issue may be in the data extraction or collection process itself.

---
*Report generated: 2026-10-23*
*Job Status: Final Attempt - No Re-run Available*
