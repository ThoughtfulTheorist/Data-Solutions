CREATE TABLE Campaign (
    CampaignID INT PRIMARY KEY IDENTITY(1,1),
    CampaignName NVARCHAR(50),
    Description NVARCHAR(255),
    StartDate DATETIME,
    EndDate DATETIME,
    CampaignType NVARCHAR(50),
    DiscountType NVARCHAR(30),
    DiscountValue FLOAT,
    MinPurchaseAmount MONEY,
    TargetProductSku INT,
    TargetCustomerSegment NVARCHAR(50),
    IsActive BIT,
    CouponCode NVARCHAR(20)
);

ALTER TABLE Campaign
ADD CONSTRAINT FK_Campaign_ProductSku
FOREIGN KEY (TargetProductSku)
REFERENCES Product(Sku);
