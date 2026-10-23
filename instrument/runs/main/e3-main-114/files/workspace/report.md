# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The data processing job encountered a critical issue: incomplete input data.

### Details
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

**Missing Records:** R001, R005, R009, R013, R017, R021

### Data Found (18 records)
- **North Region:** 304,077 cents (6 records)
- **South Region:** 300,467 cents (6 records)
- **West Region:** 287,180 cents (6 records)

### Total (Partial): 891,724 cents

### Conclusion
The job cannot be completed without all 24 records. The missing 6 records represent a 25% data gap. Data integrity requires the complete dataset before summarization can be finalized.
