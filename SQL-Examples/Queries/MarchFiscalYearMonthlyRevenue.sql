SELECT
    CASE 
        WHEN MONTH(OrderDate) >= 3 THEN YEAR(OrderDate)
        ELSE YEAR(OrderDate) - 1
    END AS FiscalYear,
    CASE 
        WHEN MONTH(OrderDate) >= 3 THEN MONTH(OrderDate) - 2
        ELSE MONTH(OrderDate) + 10
    END AS FiscalMonth,
    SUM(Amount) AS Revenue
FROM
    Transactions
GROUP BY
    CASE 
        WHEN MONTH(OrderDate) >= 3 THEN YEAR(OrderDate)
        ELSE YEAR(OrderDate) - 1
    END,
    CASE 
        WHEN MONTH(OrderDate) >= 3 THEN MONTH(OrderDate) - 2
        ELSE MONTH(OrderDate) + 10
    END
ORDER BY
    FiscalYear,
    FiscalMonth;