WITH CustomerTransactions AS (
    SELECT
        CustomerID,
        YEAR(OrderDate) AS Year,
        COUNT(*) AS Transactions
    FROM Transactions
    WHERE OrderDate BETWEEN '2020-10-28' AND '2023-10-27'
    GROUP BY CustomerID, YEAR(OrderDate)
),
CustomerYears AS (
    SELECT
        CustomerID,
        MIN(Year) AS FirstYear,
        MAX(Year) AS LastYear,
        COUNT(DISTINCT Year) AS ActiveYears
    FROM CustomerTransactions
    GROUP BY CustomerID
    HAVING COUNT(DISTINCT Year) > 1
)
SELECT
    ct.Year,
    COUNT(DISTINCT ct.CustomerID) AS TotalCustomers,
    COUNT(DISTINCT cy.CustomerID) AS ReturningCustomers,
    CAST(COUNT(DISTINCT cy.CustomerID) AS FLOAT) / COUNT(DISTINCT ct.CustomerID) * 100 AS RetentionRate
FROM CustomerTransactions ct
LEFT JOIN CustomerYears cy ON ct.CustomerID = cy.CustomerID AND ct.Year > cy.FirstYear
GROUP BY ct.Year
ORDER BY ct.Year;
