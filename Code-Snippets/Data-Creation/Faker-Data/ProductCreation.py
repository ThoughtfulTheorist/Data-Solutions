import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Create a Faker instance
fake = Faker()

# Define the number of products
num_products = 7500

# Use a set to keep track of unique Product Codes
unique_product_codes = set()

# Create empty lists to store the generated data
ProductCode = []
ItemName = []
Description = []
ProductCategory = []
UnitPrice = []
StockNew = []
StockSold = []
StockAvailable = []
DistributorID = []
DistributorName = []
DistributorContactFirstName = []
DistributorContactLastName = []
DistributorContactEmail = []
DateAdded = []
DateModified = []

# Generate the data
for _ in range(num_products):
    # Generate a unique Product Code
    while True:
        code = random.randint(1, 9999999)
        if code not in unique_product_codes:
            unique_product_codes.add(code)
            ProductCode.append(code)
            break

    # Product Name
    item_name = f"{fake.word().capitalize()} {fake.word().capitalize()}"
    ItemName.append(item_name)

    # Generate a description text and remove line breaks
    description_text = fake.text(max_nb_chars=255).replace('\n', ' ')
    Description.append(description_text)

    # Category
    category = fake.word().capitalize()
    ProductCategory.append(category)

    # Price
    price = round(random.uniform(1.00, 1000.00), 2)
    UnitPrice.append(price)

    # Stock details
    new_stock = random.randint(0, 100)
    sold_stock = random.randint(0, 100)
    available_stock = random.randint(0, 100)
    StockNew.append(new_stock)
    StockSold.append(sold_stock)
    StockAvailable.append(available_stock)

    # Supplier details
    distributor_id = random.randint(1, 1000)
    distributor_name = fake.company()
    distributor_contact_first_name = fake.first_name()
    distributor_contact_last_name = fake.last_name()
    distributor_contact_email = fake.email()
    DistributorID.append(distributor_id)
    DistributorName.append(distributor_name)
    DistributorContactFirstName.append(distributor_contact_first_name)
    DistributorContactLastName.append(distributor_contact_last_name)
    DistributorContactEmail.append(distributor_contact_email)

    # Dates
    added_date = fake.date_time_this_decade()
    modified_date = added_date + timedelta(days=random.randint(0, 365))
    DateAdded.append(added_date)
    DateModified.append(modified_date)

# Create a Pandas DataFrame
df = pd.DataFrame({
    'ProductCode': ProductCode,
    'ItemName': ItemName,
    'Description': Description,
    'Category': ProductCategory,
    'UnitPrice': UnitPrice,
    'StockIncoming': StockNew,
    'StockOutgoing': StockSold,
    'StockCurrent': StockAvailable,
    'DistributorID': DistributorID,
    'DistributorName': DistributorName,
    'ContactFirstName': DistributorContactFirstName,
    'ContactLastName': DistributorContactLastName,
    'ContactEmail': DistributorContactEmail,
    'DateAdded': DateAdded,
    'DateModified': DateModified
})

# Save the DataFrame to a CSV file
df.to_csv('UpdatedFakeProducts.csv', index=False)

print("CSV file created to contain", num_products, "rows of python-generated random product data.")
