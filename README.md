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


### Step 2 - Data Cleaning & Database Preparation 

In this step, the dataset was cleaned to ensure accurate retention analysis.

To following transformations were applied:
- Removed rows with missing Customer Id
- Excluded cancelled invoices
- Removed negative quantities ( returns )
- Removed zero or negative prices
- Converted InvoiceDate to datetime format 
- Created Revenue column (Quantity * Price)

After cleaning, the processed data was saved into a SQLite database (`customer_retention.db`) as the `orders` table.

This step ensures that further cohort analysis is based on valid and reliable transactional data.