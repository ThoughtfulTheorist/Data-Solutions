CREATE TABLE Product (
    Sku INT PRIMARY KEY,
    ProductName NVARCHAR(75),
    Sku_Desc NVARCHAR(255),
    Category NVARCHAR(25),
    Price MONEY,
    IncomingStock INT,
    OutgoingStock INT,
    OnHandStock INT,
    SupplierID INT,
    SupplierCompany NVARCHAR(50),
    SupplierFirstName NVARCHAR(25),
    SupplierLastName NVARCHAR(25),
    SupplierEmail NVARCHAR(50),
    AddedDate DATETIME,
    UpdatedDate DATETIME
);
