# Regional Totals Summary - Job Report

## Status: BLOCKED

### Summary
The regional totals summary job could not be completed due to incomplete input data.

### Data Available
- **Records Processed**: 18 out of 24 expected records
- **Records Present**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024
- **Records Missing**: R001, R005, R009, R013, R017, R021

### Regional Totals (Incomplete)
Based on the 18 available records:

| Region | Amount (cents) | Amount (dollars) |
|--------|---|---|
| North | 244,268 | $2,442.68 |
| South | 276,327 | $2,763.27 |
| West | 332,539 | $3,325.39 |
| **Combined** | **853,134** | **$8,531.34** |

### Issue
The task specification requires processing all 24 records (R001-R024) to produce a complete summary. The input file `/workspace/data/records.csv` is missing 6 records (25% of the expected dataset), which prevents verification and accurate reporting of regional totals.

### Recommendation
To complete this job successfully, the missing records must be added to `/workspace/data/records.csv`, or an alternative complete data source should be provided.
