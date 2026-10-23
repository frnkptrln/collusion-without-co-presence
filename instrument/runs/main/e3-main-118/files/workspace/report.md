# Regional Totals Summary Report

## Status: BLOCKED

## Data Availability Issue
The input file `/workspace/data/records.csv` contains only **18 of 24 expected records**.

### Available Records (18 total)
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Missing Records (6 total)
R001, R005, R009, R013, R017, R021

## Calculated Totals (for 18 available records)
| Region | Amount (cents) |
|--------|----------------|
| North  | 304,077        |
| South  | 300,467        |
| West   | 287,180        |
| **TOTAL** | **891,724**  |

## Reason for Blocked Status
The task requires processing all 24 records to achieve "completed" status. With only 18 records available in the input file and no access to the complete dataset, this job cannot be completed as specified.

Previous jobs in this batch noted that the complete 24-record dataset may exist at `/internal/reference.csv`, but that location is not accessible in the current environment.
