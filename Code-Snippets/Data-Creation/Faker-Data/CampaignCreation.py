import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Create a Faker instance
fake = Faker()

# Define the number of campaigns
num_campaigns = 7500

# Create empty lists to store the generated data
CampaignIdentifier = []
CampaignTitle = []
CampaignDescription = []
CampaignStart = []
CampaignEnd = []
TypeOfCampaign = []
TypeOfDiscount = []
ValueOfDiscount = []
MinimumPurchase = []
ProductSku = []
CustomerSegment = []
CampaignActive = []
PromoCode = []

# Generate the data
for i in range(num_campaigns):
    CampaignIdentifier.append(i + 1)
    CampaignTitle.append(fake.catch_phrase())
    CampaignDescription.append(fake.text(max_nb_chars=255).replace('\n', ' '))
    start_date = fake.date_time_this_decade()
    CampaignStart.append(start_date)
    CampaignEnd.append(start_date + timedelta(days=random.randint(30, 365)))
    TypeOfCampaign.append(random.choice(['Seasonal', 'Clearance', 'Launch', 'Special Offer']))
    TypeOfDiscount.append(random.choice(['Percentage', 'Fixed Amount']))
    ValueOfDiscount.append(round(random.uniform(5.00, 50.00), 2))
    MinimumPurchase.append(round(random.uniform(10.00, 100.00), 2))
    ProductSku.append(random.randint(1, 9999999))
    CustomerSegment.append(random.choice(['Regular', 'VIP', 'New']))
    CampaignActive.append(random.choice([0, 1]))
    PromoCode.append(fake.bothify(text='????-#####'))

# Create a Pandas DataFrame
df = pd.DataFrame({
    'ID': CampaignIdentifier,
    'Title': CampaignTitle,
    'Description': CampaignDescription,
    'Start': CampaignStart,
    'End': CampaignEnd,
    'Type': TypeOfCampaign,
    'DiscountType': TypeOfDiscount,
    'DiscountValue': ValueOfDiscount,
    'MinPurchase': MinimumPurchase,
    'Sku': ProductSku,
    'Segment': CustomerSegment,
    'Active': CampaignActive,
    'Code': PromoCode
})

# Save the DataFrame to a CSV file
df.to_csv('FakeCampaigns.csv', index=False)

print("CSV file created to contain", num_campaigns, "rows of python-generated random campaign data.")
