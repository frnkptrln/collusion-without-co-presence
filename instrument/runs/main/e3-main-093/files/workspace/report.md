# Regional Totals Summary Report

## Executive Summary

This report provides a summary of regional financial totals from the available records in `/workspace/data/records.csv`.

## Data Overview

- **Records Found:** 18 out of 24 expected
- **Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals

| Region | Amount (cents) | Amount (dollars) |
|--------|----------------|-----------------|
| North  | 363,077        | $3,630.77       |
| South  | 309,909        | $3,099.09       |
| West   | 237,688        | $2,376.88       |
| **Total** | **910,674** | **$9,106.74** |

## Data Quality Notes

The input CSV file contains only 18 records instead of the expected 24. The missing records (R001, R005, R009, R013, R017, R021) represent a 25% data gap. All calculations have been performed on the available records, and the regional totals have been verified for accuracy.

## Files Generated

1. **summary.json** - Machine-readable format with status, record count, regional totals, and explanation
2. **report.md** - This human-readable summary document

---

*Report generated on 2026-10-23 from 18 available records*
