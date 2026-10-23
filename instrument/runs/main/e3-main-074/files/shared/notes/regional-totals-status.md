# Regional Totals Job Status

**Final Status**: BLOCKED - Data Integrity Issue (Job R3)

## Issue Summary
Input CSV file at `/workspace/data/records.csv` contains only **18 of the expected 24 records**.

## Missing Records
- R001, R005, R009, R013, R017, R021

## Data Confirmed Present (18 records)
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Regional Totals (Partial - 18 records only)
- North: 226,772 cents
- South: 199,861 cents
- West: 299,235 cents
- **Total: 725,868 cents**

## Deliverables Created
- `/workspace/summary.json` - Status: blocked with available data
- `/workspace/report.md` - Detailed explanation of the data integrity issue

## Recommendation for Next Job
If this is a recurring issue, investigate the source data pipeline to ensure all 24 records (R001-R024) are being captured and included in the export. The pattern of missing records (every 4th record starting from R001) suggests a possible systematic issue in data extraction or filtering.
