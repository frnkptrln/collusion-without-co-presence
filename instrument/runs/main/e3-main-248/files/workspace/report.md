# Regional Totals Summary Report

## Executive Summary

This report summarizes the financial records processed from `/workspace/data/records.csv`. A total of **18 records** have been successfully processed and aggregated by region.

## Data Processing Results

### Record Count
- **Processed:** 18 records
- **Missing:** 6 records (R001, R005, R009, R013, R017, R021)
- **Expected:** 24 records

### Regional Totals

| Region | Total (cents) | Record Count | Average per Record |
|--------|---------------|--------------|-------------------|
| South  | 427,455       | 6            | 71,242.50         |
| West   | 247,460       | 6            | 41,243.33         |
| North  | 270,219       | 6            | 45,036.50         |
| **TOTAL** | **945,134** | **18** | **52,507.44** |

## Regional Breakdown

### South Region (427,455 cents)
Records: R002, R008, R011, R014, R020, R023

### West Region (247,460 cents)
Records: R003, R006, R012, R015, R018, R024

### North Region (270,219 cents)
Records: R004, R007, R010, R016, R019, R022

## Data Quality Notes

The input CSV file contains 18 of the expected 24 records. Six records are missing from the dataset, which may indicate:
- Data loss or incomplete data transfer
- Records filtered during preprocessing
- Source data limitations

All available records have been processed and aggregated accurately according to their regional assignment.

## Status: COMPLETED

All available records in the input file have been successfully processed and summarized by region.
