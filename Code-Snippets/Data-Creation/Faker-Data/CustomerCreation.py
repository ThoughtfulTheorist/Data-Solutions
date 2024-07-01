import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Create a Faker instance
fake = Faker()

# Define the number of customers
num_customers = 7500

# Create empty lists to store the generated data
ClientID = []
ClientFirstName = []
ClientLastName = []
ClientEmail = []
ClientPhone = []
ClientRepID = []
ProfileCreated = []
ProfileUpdated = []
HomeStreet = []
HomeUnit = []
HomeCity = []
HomeState = []
HomePostalCode = []
HomeCountry = []
DeliveryStreet = []
DeliveryUnit = []
DeliveryCity = []
DeliveryState = []
DeliveryPostalCode = []
DeliveryCountry = []

# Generate the data
for i in range(num_customers):
    ClientID.append(i + 1)
    ClientFirstName.append(fake.first_name())
    ClientLastName.append(fake.last_name())
    ClientEmail.append(fake.email())
    ClientPhone.append(fake.phone_number())
    ClientRepID.append(random.randint(1, 1000))
    created_date = fake.date_time_this_decade()
    ProfileCreated.append(created_date)
    ProfileUpdated.append(created_date + timedelta(days=random.randint(0, 365)))
    HomeStreet.append(fake.street_address())
    HomeUnit.append(fake.secondary_address() if random.random() < 0.5 else None)
    HomeCity.append(fake.city())
    HomeState.append(fake.state())
    HomePostalCode.append(fake.zipcode())
    HomeCountry.append(fake.country())
    DeliveryStreet.append(fake.street_address())
    DeliveryUnit.append(fake.secondary_address() if random.random() < 0.5 else None)
    DeliveryCity.append(fake.city())
    DeliveryState.append(fake.state())
    DeliveryPostalCode.append(fake.zipcode())
    DeliveryCountry.append(fake.country())

# Create a Pandas DataFrame
df = pd.DataFrame({
    'ClientID': ClientID,
    'FirstName': ClientFirstName,
    'LastName': ClientLastName,
    'Email': ClientEmail,
    'Phone': ClientPhone,
    'RepID': ClientRepID,
    'DateCreated': ProfileCreated,
    'DateUpdated': ProfileUpdated,
    'BillingStreet': HomeStreet,
    'BillingUnit': HomeUnit,
    'BillingCity': HomeCity,
    'BillingState': HomeState,
    'BillingPostal': HomePostalCode,
    'BillingCountry': HomeCountry,
    'ShippingStreet': DeliveryStreet,
    'ShippingUnit': DeliveryUnit,
    'ShippingCity': DeliveryCity,
    'ShippingState': DeliveryState,
    'ShippingPostal': DeliveryPostalCode,
    'ShippingCountry': DeliveryCountry
})

# Save the DataFrame to a CSV file
df.to_csv('FakeCustomers.csv', index=False)

print("CSV file created to contain", num_customers, "rows of python-generated random customer data.")
