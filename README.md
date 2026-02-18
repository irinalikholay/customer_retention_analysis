## Step 1 - Data Exploration

In this step, the Online Retail II dataset (1M+ transactions) was loaded and explored.

The following checks were performed:
- Dataset shape and structure
- Data types validation
- Missing values analysis
- Detection of negative quantities (returns)
- Detection of negative/zero prices
- Identification of cancelled invoices

## Key findings:
- 1,067,371 total rows
- 243,007 missing customer IDs
- 22,950 negative quantites (likely return)
- 6,207 zero/negative prices
- 19,494 cancelled invoices 

This step helpd identify data cleaning requirements before building the cohort model.