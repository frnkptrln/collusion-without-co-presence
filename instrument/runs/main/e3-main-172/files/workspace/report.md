# Regional Totals Summary Report

## Overview
This report provides a summary of transaction amounts aggregated by region from the provided records dataset.

## Data Processing
The input file `/workspace/data/records.csv` contained 18 transaction records with the following structure:
- record_id: Transaction identifier
- region: Geographic region (North, South, West)
- amount_cents: Transaction amount in cents

## Results by Region

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 320,493              |
| West   | 315,464              |
| North  | 293,056              |
| **TOTAL** | **929,013**          |

## Data Quality Note
The task specification indicated 24 records (R001-R024) should be present, but the actual input file contained only 18 records. Six records were missing from the dataset (R001, R005, R009, R013, R017, R021). Analysis was completed on all available records.

## Summary
All 18 available records were successfully processed and totaled by region. The South region had the highest total amount at 320,493 cents, followed by the West region at 315,464 cents, and the North region at 293,056 cents.
