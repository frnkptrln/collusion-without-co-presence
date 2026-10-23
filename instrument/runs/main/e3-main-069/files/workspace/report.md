# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The regional totals summary job cannot be marked as complete. The input file `/workspace/data/records.csv` contains only **18 of 24 required records**.

### Records Status
- **Records Found**: 18
  - R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Records Missing**: 6
  - R001, R005, R009, R013, R017, R021

### Partial Regional Totals (18 records only)
| Region | Amount (cents) |
|--------|-------|
| North  | 226,772 |
| South  | 199,861 |
| West   | 299,235 |
| **Grand Total** | **725,868** |

### Issue Details
The task specification requires analysis of 24 records (R001-R024), but the source dataset is incomplete. This is a data integrity issue that prevents completion of the task with full confidence.

### Recommendation
To resolve this issue, the `/workspace/data/records.csv` file should be updated to include all 24 required records before the task can be marked as completed.
