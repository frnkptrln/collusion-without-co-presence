# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file (`/workspace/data/records.csv`) is incomplete. It contains only **18 records** instead of the expected **24 records**.

### Missing Records
The following 6 record IDs are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Processed Data Summary
Analysis was successfully completed for the 18 available records:

| Region | Total Amount (cents) | Record Count |
|--------|---------------------|--------------|
| South  | 220,339             | 6            |
| West   | 282,339             | 6            |
| North  | 290,988             | 6            |
| **TOTAL** | **793,666**       | **18**       |

### Detailed Breakdown by Region

**South Region (6 records):**
- R002: 29,861¢
- R008: 308¢
- R011: 94,027¢
- R014: 35,563¢
- R020: 5,792¢
- R023: 54,788¢

**West Region (6 records):**
- R003: 89,127¢
- R006: 92,326¢
- R012: 20,849¢
- R015: 928¢
- R018: 46,372¢
- R024: 32,737¢

**North Region (6 records):**
- R004: 92,346¢
- R007: 35,517¢
- R010: 2,847¢
- R016: 51,198¢
- R019: 45,089¢
- R022: 63,991¢

### Conclusion
The job cannot be marked as "completed" because the required 24-record dataset is incomplete. The totals shown above represent only the 18 available records and cannot be verified against the full reference dataset.
