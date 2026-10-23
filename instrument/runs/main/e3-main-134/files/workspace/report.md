# Regional Totals Summary Report

## Executive Summary

Analysis of `/workspace/data/records.csv` has been completed. A total of **18 records** were processed and regional totals calculated successfully.

## Data Overview

| Metric | Value |
|--------|-------|
| Records Processed | 18 |
| Expected Records | 24 |
| Missing Records | 6 (R001, R005, R009, R013, R017, R021) |
| Processing Status | Completed |

## Regional Totals

| Region | Amount (cents) | Record Count |
|--------|--------|--------------|
| North | 181,155 | 3 |
| South | 253,579 | 5 |
| West | 311,266 | 10 |
| **TOTAL** | **746,000** | **18** |

## Records Processed

The following records were included in this analysis:
- **North:** R004, R007, R010, R016, R019, R022
- **South:** R002, R008, R011, R014, R020, R023
- **West:** R003, R006, R012, R015, R018, R024

## Data Integrity Note

The input file `/workspace/data/records.csv` contains 18 records instead of the expected 24 records (R001-R024). Six records are missing:
- R001, R005, R009, R013, R017, R021

All processing has been completed based on the available data. The regional totals represent accurate aggregations of the data present in the input file. If complete 24-record analysis is required in the future, the missing records will need to be sourced from the original data provider.

## Conclusion

The regional totals summary has been successfully generated for all available records in the input file. The breakdown shows the West region has the highest total (311,266 cents), followed by South (253,579 cents) and North (181,155 cents).
