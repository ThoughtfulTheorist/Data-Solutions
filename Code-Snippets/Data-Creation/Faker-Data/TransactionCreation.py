import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Create a Faker instance
fake = Faker()

# Define the number of transactions
num_transactions = 7500

# Create empty lists to store the generated data
DealID = []
BuyerID = []
ProductID = []
ItemCount = []
TotalCost = []
PurchaseDate = []
PurchaseSource = []
MethodOfPayment = []
PromoCampaignID = []
PromotionCode = []
PriceCutType = []
PriceCutValue = []
BillingRoad = []
BillingUnit = []
BillingTown = []
BillingRegion = []
BillingPostalCode = []
BillingNation = []
DeliveryRoad = []
DeliveryUnit = []
DeliveryTown = []
DeliveryRegion = []
DeliveryPostalCode = []
DeliveryNation = []
TransactionStatus = []
AssociateID = []

# Generate the data
for i in range(num_transactions):
    DealID.append(i + 1)
    BuyerID.append(random.randint(1, 1000))
    ProductID.append(random.randint(1, 9999999))
    ItemCount.append(random.randint(1, 10))
    TotalCost.append(round(random.uniform(10.00, 1000.00), 2))
    PurchaseDate.append(fake.date_time_this_decade())
    PurchaseSource.append(random.choice(['Online', 'In-Store', 'Mobile']))
    MethodOfPayment.append(random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']))
    PromoCampaignID.append(random.randint(1, 100) if random.random() < 0.5 else None)
    PromotionCode.append(fake.bothify(text='????-#####') if random.random() < 0.5 else None)
    PriceCutType.append(random.choice(['Percentage', 'Fixed Amount']) if random.random() < 0.5 else None)
    PriceCutValue.append(round(random.uniform(1.00, 50.00), 2) if PriceCutType[-1] else None)
    BillingRoad.append(fake.street_address())
    BillingUnit.append(fake.secondary_address() if random.random() < 0.5 else None)
    BillingTown.append(fake.city())
    BillingRegion.append(fake.state())
    BillingPostalCode.append(fake.zipcode())
    BillingNation.append(fake.country())
    DeliveryRoad.append(fake.street_address())
    DeliveryUnit.append(fake.secondary_address() if random.random() < 0.5 else None)
    DeliveryTown.append(fake.city())
    DeliveryRegion.append(fake.state())
    DeliveryPostalCode.append(fake.zipcode())
    DeliveryNation.append(fake.country())
    TransactionStatus.append(random.choice(['Pending', 'Completed', 'Shipped', 'Cancelled']))
    AssociateID.append(random.randint(1, 100) if random.random() < 0.5 else None)

# Create a Pandas DataFrame
df = pd.DataFrame({
    'TransactionID': DealID,
    'CustomerID': BuyerID,
    'ProductID': ProductID,
    'Quantity': ItemCount,
    'Amount': TotalCost,
    'DateOfOrder': PurchaseDate,
    'SourceOfOrder': PurchaseSource,
    'PaymentMethod': MethodOfPayment,
    'CampaignID': PromoCampaignID,
    'Code': PromotionCode,
    'DiscountType': PriceCutType,
    'DiscountAmount': PriceCutValue,
    'BillingStreet': BillingRoad,
    'BillingSuite': BillingUnit,
    'BillingCity': BillingTown,
    'BillingState': BillingRegion,
    'BillingZip': BillingPostalCode,
    'BillingCountry': BillingNation,
    'ShippingStreet': DeliveryRoad,
    'ShippingSuite': DeliveryUnit,
    'ShippingCity': DeliveryTown,
    'ShippingState': DeliveryRegion,
    'ShippingZip': DeliveryPostalCode,
    'ShippingCountry': DeliveryNation,
    'Status': TransactionStatus,
    'SalesRepID': AssociateID
})

# Save the DataFrame to a CSV file
df.to_csv('FakeTransactions.csv', index=False)

print("CSV file created to contain", num_transactions, "rows of python-generated random transaction data.")
