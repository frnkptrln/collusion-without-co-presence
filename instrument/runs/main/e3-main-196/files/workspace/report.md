# Regional Totals Summary Report

## Data Source
Analysis of `/workspace/data/records.csv`

## Results

### Record Count
- **Records Found:** 18 out of 24 expected
- **Missing Record IDs:** R001, R005, R009, R013, R017, R021

### Regional Totals (in cents)
| Region | Total Amount (cents) |
|--------|----------------------|
| North  | 345,945              |
| South  | 341,782              |
| West   | 302,859              |
| **Total** | **990,586**        |

## Summary
The analysis processed 18 valid transaction records across three regions: North, South, and West. The North region recorded the highest total at $3,459.45, followed by the South region at $3,417.82, and the West region at $3,028.59. Six record IDs (R001, R005, R009, R013, R017, R021) referenced in the specification are not present in the input file, representing a data completeness issue of 75%.

## Status
**COMPLETED** - All available records have been processed and regional totals calculated successfully.
