CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    Sku INT NOT NULL,
    Quantity INT NOT NULL,
    Amount MONEY NOT NULL,
    OrderDate DATETIME NOT NULL,
    OrderSource NVARCHAR(20),
    PaymentType NVARCHAR(50),
    CampaignID INT,
    CouponCode NVARCHAR(20),
    DiscountType NVARCHAR(30),
    DiscountValue DECIMAL(10,2),
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
    ShippingCountry NVARCHAR(50),
    OrderStatus NVARCHAR(20),
    SalesRep INT
);

ALTER TABLE Transactions
ADD CONSTRAINT FK_Transactions_CustomerID
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);

ALTER TABLE Transactions
ADD CONSTRAINT FK_Transactions_Sku
FOREIGN KEY (Sku) REFERENCES Product(Sku);

ALTER TABLE Transactions
ADD CONSTRAINT FK_Transactions_CampaignID
FOREIGN KEY (CampaignID) REFERENCES Campaign(CampaignID);

ALTER TABLE Transactions
ADD CONSTRAINT FK_Transactions_SalesRep
FOREIGN KEY (SalesRep) REFERENCES Employee(EmployeeID);
