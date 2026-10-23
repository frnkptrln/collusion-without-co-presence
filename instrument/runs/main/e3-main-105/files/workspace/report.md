# Regional Totals Summary Report

**Date**: 2026-10-23  
**Status**: BLOCKED - Data Integrity Issue  
**Records Available**: 18 of 24 expected  

## Executive Summary

The requested analysis of regional sales totals cannot be completed as specified due to incomplete input data. The input file `/workspace/data/records.csv` contains only 18 of the 24 records referenced in the task description (R001-R024).

## Data Status

**Available Records**: 18 records successfully processed
- R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

**Missing Records**: 6 records
- R001, R005, R009, R013, R017, R021

## Regional Totals (18 Records Only)

| Region | Amount (cents) | Record Count |
|--------|---|---|
| North | 304,077 | 6 |
| South | 300,467 | 6 |
| West | 287,180 | 6 |
| **TOTAL** | **891,724** | **18** |

## Issue Analysis

The task specifies input of 24 records (R001-R024), but the provided input file contains only 18. This prevents validation against the expected complete dataset. The missing 6 records represent 25% of the expected data volume.

## Recommendation

To complete this task successfully, either:
1. Provide the complete input file with all 24 records (R001-R024), or
2. Provide access to reference data for validation of the complete dataset

Without the missing records or access to reference data, the task cannot be marked as completed.
