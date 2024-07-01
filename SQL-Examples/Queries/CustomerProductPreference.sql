SELECT 
    customer_id,
    product_id,
    EXTRACT(YEAR FROM purchase_date) AS year,
    EXTRACT(MONTH FROM purchase_date) AS month,
    SUM(quantity) AS total_quantity
FROM 
    Transactions
WHERE 
    purchase_date >= '2021-01-01'
GROUP BY 
    customer_id,
    product_id,
    EXTRACT(YEAR FROM purchase_date),
    EXTRACT(MONTH FROM purchase_date)
ORDER BY 
    customer_id,
    year,
    month;
