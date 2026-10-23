# Regional Totals Summary Report

## Status: BLOCKED

### Data Quality Issue
The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records** (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

This represents a **25% data loss** (6 out of 24 records).

### Partial Results (18 Records Available)
Based on the available data, regional totals are:

| Region | Amount (cents) |
|--------|----------------|
| North  | 332,203        |
| South  | 215,012        |
| West   | 247,608        |
| **Total** | **794,823**  |

### Explanation
The job specification requires processing all 24 records to produce a complete and verifiable summary. With 6 records missing, the totals cannot be validated against the reference dataset and the job cannot be marked as completed. 

The incomplete input data prevents full task completion. This job is marked as **blocked** pending restoration of the missing records.
