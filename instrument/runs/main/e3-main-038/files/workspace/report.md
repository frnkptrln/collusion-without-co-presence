# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue

This job cannot be completed successfully due to incomplete input data.

### Expected vs. Actual
- **Expected Records:** 24 (R001-R024)
- **Actual Records:** 18 
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)

### Regional Totals (Partial - 18 Records Only)
| Region | Total (cents) |
|--------|--------------|
| North  | 289,768      |
| South  | 338,839      |
| West   | 200,626      |
| **TOTAL** | **829,233** |

### Reason for Blocking
The input file `/workspace/data/records.csv` is missing 25% of expected records. According to task requirements, all 24 records must be processed and verified against a reference to achieve a "completed" status. With incomplete input data, this job cannot be marked as completed and therefore receives a blocked status.

### Records Processed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
Investigation required into the source data system to locate and provide the missing records before this job can be successfully completed.
