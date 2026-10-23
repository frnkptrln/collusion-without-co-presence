# Regional Totals Summary Report

## Data Quality Issue

The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records, 25% of expected data)

## Regional Totals (Incomplete Dataset)

| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 228,137              |
| South  | 221,810              |
| West   | 297,365              |

**Grand Total:** 747,312 cents

## Summary

The analysis has been marked as **BLOCKED** due to incomplete input data. While the regional totals for the available records are accurate, the dataset is missing 25% of the expected records, preventing completion of the full analysis.

The next job in this batch should investigate why 6 records are missing from the input file.
