# Regional Totals Summary Report

## Executive Summary

**Status:** BLOCKED - Task cannot be completed due to incomplete input data.

The input file `/workspace/data/records.csv` contains only 18 of the 24 expected records (75% of expected data).

## Data Analysis

### Records Found
- **Total records in CSV:** 18
- **Record IDs present:** R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Records Missing
- **Missing record count:** 6
- **Missing record IDs:** R001, R005, R009, R013, R017, R021
- **Data gap:** 25% of expected records are unavailable

## Regional Totals (18 Records Available)

| Region | Total (cents) | Count |
|--------|---------------|-------|
| North  | 363,077       | 6     |
| South  | 309,909       | 5     |
| West   | 237,688       | 7     |
| **TOTAL** | **910,674** | **18** |

## Data Quality Issues

The input CSV file appears to have a data integrity issue with 6 missing record IDs from the expected R001-R024 range. This prevents full completion of the task as specified (which requires all 24 records).

### Note for Next Job
The data constraint (missing records R001, R005, R009, R013, R017, R021) is structural and consistent across attempts. The source of these missing records should be investigated if this task is to be retried.

---
*Report generated: 2026-10-23*
*User: frank.peterlein@gmail.com*
