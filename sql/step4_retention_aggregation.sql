-- Step 4 - Retention Aggregation

WITH retention AS (
    SELECT
        cohort_month,
        month_since_first_purchase,
        COUNT(DISTINCT customer_id) AS active_customers
    FROM cohort_data
    GROUP BY cohort_month, month_since_first_purchase
)

SELECT *
FROM retention 
ORDER BY cohort_month, month_since_first_purchase;