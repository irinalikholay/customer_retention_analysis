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

## Step 3 - Cohort Preparation

In this step we prepared the dataset for customer retention analysis.

Using SQL, we created a cohort_based structuree that allows tracking customer behavior over time.

# What was done:
- Identified each customers first purchase date
- Assigned customers to a cohort month (first_purchase_month)
- Calculated the number of months since the first purchase
- Created a derived table `cohot_data`in SQLite

# Logic:
For each customer:
- `cohort_month` - month of first puschase
- `order_month` - month of each transaction 
- `month_since_first_purchase` - difference in months between first purchase and transaction

This table serves as the foundation for building the retention matrix.

## Result:
A new table `cohort_data`was created in the database .

customer_retention.db
|__ orders
|__ cohort_data