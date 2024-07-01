import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data from CSV
data = pd.read_csv('weather_data.csv')
dates = pd.to_datetime(data['Date'])
temperatures = data['Temperature']
humidities = data['Humidity']

# Calculate moving averages
window_size = 5  # window size for moving average
temp_averages = temperatures.rolling(window=window_size).mean()
hum_averages = humidities.rolling(window=window_size).mean()

# Create side-by-side bar chart
fig, ax = plt.subplots()

# Width of a bar
bar_width = 0.35

# Positions of the bars
temp_positions = np.arange(len(dates))
hum_positions = [x + bar_width for x in temp_positions]

# Plot temperature and humidity data as side-by-side bars
# Swapped colors: temperature now uses the original humidity color, and humidity uses light blue
bars = ax.bar(temp_positions, temperatures, width=bar_width, label='Temperature (°F)', color='orange', alpha=0.7)
bars2 = ax.bar(hum_positions, humidities, width=bar_width, label='Humidity (%)', color='lightblue', alpha=1.0)

# Plot trend lines for average temperature and humidity
ax.plot(temp_positions, temp_averages, color='red', label='Avg. Temperature Trend', linestyle='--')
ax.plot(hum_positions, hum_averages, color='blue', label='Avg. Humidity Trend', linestyle='--')

# Set x-axis ticks to be in the middle of the groups of bars
ax.set_xticks([p + bar_width / 2 for p in temp_positions])
ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in dates])

# Rotate date labels for better visibility
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# Legend
ax.legend()

# Labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Values')
plt.title('Weather Data Trends: Temperature and Humidity')

# Show the plot
plt.show()
