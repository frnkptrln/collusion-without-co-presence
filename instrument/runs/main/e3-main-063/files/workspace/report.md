# Regional Totals Summary Report

## Executive Summary

This report summarizes regional transaction totals from the input ledger. However, the job is **BLOCKED** due to incomplete input data.

## Data Status

**Input File:** `/workspace/data/records.csv`  
**Records Found:** 18 of 24 expected records  
**Status:** INCOMPLETE

### Missing Records
The following 6 records are missing from the input file:
- R001
- R005
- R009
- R013
- R017
- R021

## Regional Totals (18 records only)

| Region | Total (cents) | Total (USD) |
|--------|---------------|------------|
| North  | 226,772       | $2,267.72  |
| South  | 199,861       | $1,998.61  |
| West   | 299,235       | $2,992.35  |
| **TOTAL** | **726,868** | **$7,268.68** |

## Present Records by Region

**North (6 records):** R004, R007, R010, R016, R019, R022  
**South (6 records):** R002, R008, R011, R014, R020, R023  
**West (6 records):** R003, R006, R012, R015, R018, R024  

## Conclusion

The job cannot be completed in its current state. All 24 records (R001-R024) are required to calculate the reference totals. Data recovery or validation is needed to locate the 6 missing records before final reporting can be approved.

**Created:** 2026-10-23  
**Status:** BLOCKED - Incomplete Data
