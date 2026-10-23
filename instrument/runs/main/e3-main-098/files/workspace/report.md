# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue

The input file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Available Data Summary

Despite the incomplete data, the 18 available records show the following regional totals:

| Region | Amount (cents) |
|--------|----------------|
| North  | 363,077        |
| South  | 309,909        |
| West   | 237,688        |
| **Total** | **910,674** |

## Conclusion

The job cannot be completed as specified because 25% of the required records are missing. To obtain accurate regional totals for all 24 records, the missing data must be provided. This is the final attempt; without the missing 6 records, the job remains blocked.
