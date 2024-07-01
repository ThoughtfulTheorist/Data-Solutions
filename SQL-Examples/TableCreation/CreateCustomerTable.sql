CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(25),
    LastName NVARCHAR(25),
    Email NVARCHAR(50),
    Phone NVARCHAR(20),
    AccountManager INT,
    CreatedDate DATETIME NOT NULL,
    LastUpdated DATETIME,
    BillingStreet NVARCHAR(50),
    BillingAptSuite NVARCHAR(50),
    BillingCity NVARCHAR(50),
    BillingState NVARCHAR(50),
    BillingZip NVARCHAR(10),
    BillingCountry NVARCHAR(50),
    ShippingStreet NVARCHAR(50),
    ShippingAptSuite NVARCHAR(50),
    ShippingCity NVARCHAR(50),
    ShippingState NVARCHAR(50),
    ShippingZip NVARCHAR(10),
    ShippingCountry NVARCHAR(50)
);

ALTER TABLE Customer
ADD CONSTRAINT FK_Customer_AccountManager
FOREIGN KEY (AccountManager) REFERENCES Employee(EmployeeID);
