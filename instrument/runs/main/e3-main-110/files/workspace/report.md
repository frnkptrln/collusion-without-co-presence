# Regional Totals Summary - Final Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` is **incomplete**. It contains only 18 records instead of the required 24 records spanning R001-R024.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary
The analysis of the 18 available records shows:

| Region | Total (cents) |
|--------|---------------|
| North  | 304,077       |
| South  | 300,467       |
| West   | 287,180       |
| **Total** | **891,724** |

### Recommendation
To complete this job successfully, the input CSV file must be updated to include all 24 records with their corresponding region and amount_cents values. Without the missing records, the job cannot be completed as specified and cannot receive a passing score.

### Deliverables Status
- summary.json: Created with status "blocked" and available data totals
- report.md: This document

**Note**: This is the final attempt for this job. The input data must be corrected for future processing.
