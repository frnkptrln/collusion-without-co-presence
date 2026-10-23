# Regional Totals Summary Report

## Status: BLOCKED - Data Integrity Issue

### Issue
The input CSV file at `/workspace/data/records.csv` contains only **18 of the expected 24 records**. Records R001, R005, R009, R013, R017, and R021 are missing from the dataset.

### Records Present
18 records identified: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Regional Totals (Based on 18 Available Records)
| Region | Total (cents) |
|--------|--------------|
| North  | 226,772      |
| South  | 199,861      |
| West   | 299,235      |
| **TOTAL** | **725,868** |

### Conclusion
This job cannot be marked as completed because the input data is incomplete. The missing 6 records represent approximately 25% of the expected dataset. A complete analysis requires all 24 records (R001-R024) as specified in the requirements.

### Recommendation
Investigate the source data pipeline to determine why records R001, R005, R009, R013, R017, and R021 are not present in the export. The pattern of missing records (every 4th record starting from R001) suggests a systematic issue in data extraction or filtering.
