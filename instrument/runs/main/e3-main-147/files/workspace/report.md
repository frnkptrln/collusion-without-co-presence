# Regional Totals Summary Report

## Overview
This report summarizes the regional financial data from the records file.

## Data Summary
- **Records Processed:** 18 out of expected 24
- **Missing Records:** R001, R005, R009, R013, R017, R021
- **Source File:** /workspace/data/records.csv

## Regional Totals

| Region | Total (cents) |
|--------|---------------|
| South  | 220,339       |
| West   | 282,339       |
| North  | 290,988       |
| **Grand Total** | **793,666** |

## Findings
The dataset contains 18 complete transaction records spanning three regions (North, South, and West). Six record IDs (R001, R005, R009, R013, R017, R021) are absent from the input file, resulting in incomplete coverage of the expected 24-record dataset.

The regional distribution shows:
- West region has the highest total at 282,339 cents
- North region follows with 290,988 cents  
- South region accounts for 220,339 cents

## Data Quality Notes
The input file appears to be missing records for IDs at regular intervals (every 4th record in the sequence). This pattern suggests a potential data collection or transmission issue that should be investigated for the complete dataset.

All calculations are based on the 18 records available in the current data file.
