import pandas as pd
import random
from faker import Faker
from datetime import timedelta, date

# Create a Faker instance
fake = Faker()

# Define the number of days for which you want to generate weather data
num_days = 30

# Lists to store generated data
dates = []
temperatures = []
humidities = []

# Base temperature and humidity
base_temperature = random.uniform(20.0, 25.0)  # Base temperature in degrees Celsius
base_humidity = random.uniform(50.0, 60.0)     # Base humidity in percentage

# Convert base temperature to Fahrenheit and round it
base_temperature = round(base_temperature * 9/5 + 32, 2)

# Generate a starting date
start_date = fake.date_this_month()

# Check if start_date is not a date object and convert if necessary
if isinstance(start_date, str):
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()

# Generate weather data with controlled variability
for i in range(num_days):
    current_date = start_date + timedelta(days=i)
    dates.append(current_date.strftime('%Y-%m-%d'))  # Format date as string

    # Generate temperature and humidity with controlled changes
    if i > 0:
        temperature_change = random.uniform(-2.0, 2.0)
        # Convert temperature change to Fahrenheit scale (since it's a delta, only scale, no addition of 32 needed)
        temperature_change = temperature_change * 9/5
        humidity_change = random.uniform(-5.0, 5.0)
        temperature = max((15.0 * 9/5 + 32), min((35.0 * 9/5 + 32), temperatures[-1] + temperature_change))
        humidity = max(30.0, min(90.0, humidities[-1] + humidity_change))
    else:
        temperature = base_temperature
        humidity = base_humidity

    # Round temperature and humidity to 2 decimal places
    temperature = round(temperature, 2)
    humidity = round(humidity, 2)

    # Append temperature and humidity data to lists
    temperatures.append(temperature)
    humidities.append(humidity)

# Create a Pandas DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Temperature': temperatures,
    'Humidity': humidities
})

# Save the DataFrame to a CSV file
df.to_csv('weather_data.csv', index=False)

print("CSV file created containing", num_days, "days of generated weather data, starting from", start_date.strftime('%Y-%m-%d'))
