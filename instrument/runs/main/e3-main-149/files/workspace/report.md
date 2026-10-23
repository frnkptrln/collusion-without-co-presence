# Regional Totals Summary Report

## Status: BLOCKED

## Summary

The regional totals job has encountered a data integrity issue that prevents completion. The input CSV file contains only **18 records** instead of the expected **24 records** (R001-R024).

## Data Processed

The following 18 records were successfully processed:

| Region | Record Count | Total (cents) |
|--------|-------------|---------------|
| South  | 6           | 220,339       |
| West   | 6           | 282,339       |
| North  | 6           | 290,988       |
| **TOTAL** | **18**    | **793,666**   |

## Missing Records

The following 6 records are missing from the input file:
- R001
- R005
- R009
- R013
- R017
- R021

## Records Present

**South Region (6 records):** R002, R008, R011, R014, R020, R023
**West Region (6 records):** R003, R006, R012, R015, R018, R024
**North Region (6 records):** R004, R007, R010, R016, R019, R022

## Conclusion

To complete this job successfully, all 24 records must be present in the input file. The current dataset is incomplete and cannot be verified against the full reference totals.
