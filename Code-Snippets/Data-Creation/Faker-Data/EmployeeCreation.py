import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# Create a Faker instance
fake = Faker()

# Define the number of employees
num_employees = 7500

# Create empty lists to store the generated data
StaffID = []
GivenName = []
Surname = []
ContactEmail = []
ContactPhone = []
StartDay = []
EndDay = []
WorkArea = []
JobTitle = []
PayScale = []
BonusRate = []
TargetSales = []
RealizedSales = []
EmploymentStatus = []
ResidenceStreet = []
ResidenceCity = []
ResidenceState = []
ResidencePostal = []
ResidenceCountry = []
CoverageHealth = []
CoverageDental = []
PlanRetirement = []

# Generate the data
for i in range(num_employees):
    StaffID.append(i + 1)
    GivenName.append(fake.first_name())
    Surname.append(fake.last_name())
    ContactEmail.append(fake.email())
    ContactPhone.append(fake.phone_number())
    hire_date = fake.date_time_this_decade()
    StartDay.append(hire_date)
    EndDay.append(hire_date + timedelta(days=random.randint(0, 3650)) if random.random() < 0.1 else None)
    WorkArea.append(random.choice(['Sales', 'Engineering', 'HR', 'Marketing', 'Finance', 'Customer Support']))
    JobTitle.append(random.choice(['Manager', 'Developer', 'Analyst', 'Specialist', 'Coordinator', 'Executive']))
    PayScale.append(round(random.uniform(30000.00, 120000.00), 2))
    BonusRate.append(round(random.uniform(0.00, 20.00), 2))
    TargetSales.append(round(random.uniform(50000.00, 1000000.00), 2))
    RealizedSales.append(0.00)  # Default value
    EmploymentStatus.append(random.choice(['Active', 'Inactive']))
    ResidenceStreet.append(fake.street_address())
    ResidenceCity.append(fake.city())
    ResidenceState.append(fake.state())
    ResidencePostal.append(fake.zipcode())
    ResidenceCountry.append(fake.country())
    CoverageHealth.append(random.choice([0, 1]))
    CoverageDental.append(random.choice([0, 1]))
    PlanRetirement.append(random.choice([0, 1]))

# Create a Pandas DataFrame
df = pd.DataFrame({
    'StaffID': StaffID,
    'Name': GivenName,
    'Surname': Surname,
    'Email': ContactEmail,
    'Phone': ContactPhone,
    'StartDate': StartDay,
    'EndDate': EndDay,
    'Department': WorkArea,
    'Position': JobTitle,
    'Salary': PayScale,
    'Commission': BonusRate,
    'SalesGoal': TargetSales,
    'SalesAchieved': RealizedSales,
    'Status': EmploymentStatus,
    'Address': ResidenceStreet,
    'City': ResidenceCity,
    'State': ResidenceState,
    'PostalCode': ResidencePostal,
    'Country': ResidenceCountry,
    'HealthInsurance': CoverageHealth,
    'DentalInsurance': CoverageDental,
    'RetirementPlan': PlanRetirement
})

# Save the DataFrame to a CSV file
df.to_csv('FakeEmployees.csv', index=False)

print("CSV file created to contain", num_employees, "rows of python-generated random employee data.")
