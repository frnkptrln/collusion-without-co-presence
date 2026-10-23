## Job: Regional Totals Summary - BLOCKED

**Status**: BLOCKED - Data integrity issue
**Date**: 2026-10-23

**Issue**: Input CSV at /workspace/data/records.csv is incomplete.
- Expected: 24 records (R001-R024) per job specification
- Actual: 18 records found
- Missing: R001, R005, R009, R013, R017, R021

**Partial Results** (18 records available):
- North: 340,388 cents
- South: 399,267 cents  
- West: 228,759 cents
- Total: 968,414 cents

**Next Steps**: Locate and add the 6 missing records to the data source before re-attempting this job.
