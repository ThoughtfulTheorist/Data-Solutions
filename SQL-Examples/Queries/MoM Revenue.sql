WITH MonthlyRevenue AS (
    SELECT
        YEAR(OrderDate) AS Year,
        MONTH(OrderDate) AS Month,
        SUM(Amount) AS Revenue
    FROM
        Transactions
    GROUP BY
        YEAR(OrderDate),
        MONTH(OrderDate)
)

SELECT
    Current.Year,
    Current.Month,
    Current.Revenue,
    COALESCE((Current.Revenue - Previous.Revenue) / NULLIF(Previous.Revenue, 0), 0) AS MoM_Growth
FROM
    MonthlyRevenue AS Current
LEFT JOIN
    MonthlyRevenue AS Previous ON (Current.Year = Previous.Year AND Current.Month = Previous.Month + 1)
    OR (Current.Year = Previous.Year + 1 AND Current.Month = 1 AND Previous.Month = 12)
ORDER BY
    Current.Year,
    Current.Month;
