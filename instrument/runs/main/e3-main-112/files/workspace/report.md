# Regional Totals Summary Report

## Status: BLOCKED

## Data Summary

The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records**.

### Missing Records
The following 6 records are missing from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Records
18 records were successfully processed (R002-R024, excluding the missing ones above).

## Regional Totals (for 18 available records)

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 304,077       | 6            |
| South  | 300,467       | 6            |
| West   | 287,180       | 6            |
| **Total** | **891,724** | **18**       |

## Issue

The job cannot be marked as "completed" because 6 of the 24 expected records are missing from the input data. To resolve this issue and achieve completion, the missing records need to be added to the CSV file.
