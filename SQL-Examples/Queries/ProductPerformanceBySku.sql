WITH YearlyOrders AS (
   SELECT
       YEAR(t.OrderDate) AS year,
       MONTH(t.OrderDate) AS month,
       COUNT(DISTINCT t.OrderDate) AS DistinctDates
   FROM Transactions t
   WHERE t.OrderDate BETWEEN '2024-01-01' AND '2024-12-31'
   GROUP BY YEAR(t.OrderDate), MONTH(t.OrderDate)
),

MonthlyItemOrders AS (
   SELECT
       YEAR(t.OrderDate) AS year,
       MONTH(t.OrderDate) AS month,
       t.Sku AS Item,
       COUNT(DISTINCT t.TransactionID) AS Orders,
       SUM(t.Amount) AS Revenue
   FROM Transactions t
   INNER JOIN Product p ON t.Sku = p.Sku
   WHERE p.Sku_Desc LIKE '%ExampleSku1%' OR p.Sku_Desc LIKE '%ExampleSku2%'
   GROUP BY YEAR(t.OrderDate), MONTH(t.OrderDate), t.Sku
)

SELECT y.year, y.month, m.Item, SUM(m.Orders) AS TotalOrders, SUM(m.Revenue) AS TotalRevenue
FROM YearlyOrders y
LEFT JOIN MonthlyItemOrders m ON y.year = m.year AND y.month = m.month
GROUP BY y.year, y.month, m.Item
ORDER BY y.year, y.month, m.Item;
