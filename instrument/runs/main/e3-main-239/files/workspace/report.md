# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue
The regional totals summary job cannot be completed due to incomplete input data.

### Summary
- **Expected Records:** 24 (R001-R024)
- **Actual Records:** 18
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)
- **Completion Rate:** 75%

### Totals by Region (18 Available Records)
| Region | Total (cents) |
|--------|--------------|
| North  | 220,421      |
| South  | 231,872      |
| West   | 387,930      |
| **TOTAL** | **840,223** |

### Root Cause
Six records are missing from the input CSV file. These records have not been located in any available workspace or shared directories. The data source must be checked to retrieve the missing records before this job can be completed.

### Recommendation
Please verify the data source and provide all 24 records to complete the regional totals summary.

---
*Report generated: 2026-10-23*  
*Status: BLOCKED - Awaiting missing records*
