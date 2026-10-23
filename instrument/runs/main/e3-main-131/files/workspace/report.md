# Regional Totals Summary Report

## Overview
This report summarizes transaction records by region from the input dataset.

## Data Summary
- **Records Processed:** 18 records
- **Records Expected:** 24 records (R001-R024)
- **Data Status:** Incomplete - 6 records missing (R001, R005, R009, R013, R017, R021)

## Regional Totals (in cents)
| Region | Total Amount |
|--------|--------------|
| North  | 181,155      |
| South  | 253,579      |
| West   | 311,266      |
| **Total** | **746,000** |

## Findings
The analysis processed all available records from the input file `/workspace/data/records.csv`. The South and West regions account for approximately 67% of total transaction value, while the North region accounts for approximately 24%. 

**Note:** The input data was incomplete, containing only 18 of the expected 24 records. Six record IDs (R001, R005, R009, R013, R017, R021) were not present in the source file.
