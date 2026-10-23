# Regional Totals Summary Report

## Status: BLOCKED

## Summary
This job cannot be completed as specified due to incomplete input data.

## Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the required 24 records (R001-R024).

### Missing Records
- R001, R005, R009, R013, R017, R021

## Available Data
The CSV file contains the following 18 records with regional totals:

| Region | Total (cents) |
|--------|--------------|
| North  | 304,077      |
| South  | 300,467      |
| West   | 287,180      |

**Combined Total:** 891,724 cents

## Reason for Blocking
The job requirements specify "24 records R001-R024" but the input data is missing 6 records. Without access to the missing records or their reference data, it is impossible to calculate the correct regional totals for the complete dataset. Proceeding with partial data would not meet the job specifications.

## Recommendation
Verify and provide the complete input dataset containing all 24 records before attempting to complete this job.
