SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Email,
    c.Phone,
    COUNT(t.TransactionID) AS EmailTransactionCount,
    MAX(t.OrderDate) AS LastEmailTransactionDate
FROM Customers c
JOIN Transactions t ON c.CustomerID = t.CustomerID
WHERE t.OrderSource = 'Email'
GROUP BY 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Email,
    c.Phone;
