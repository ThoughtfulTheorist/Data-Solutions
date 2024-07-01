# MatPlotLibWeather
This project generates synthetic weather data and visualizes it using bar charts.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed on your machine:
- Python 3.6 or higher
- `pandas` library
- `matplotlib` library
- `Faker` library

You can install the required Python libraries using the following command:

```bash
pip install pandas matplotlib Faker
Installation
Clone the repository:

bash
Always show details

Copy code
git clone https://github.com/ThoughtfulTheorist/MatPlotLibWeather
cd weather-data
Running the Scripts:

Step 1: Generate Weather Data

To generate the weather data, run the WeatherGeneration.py script:

bash
Always show details

Copy code
python WeatherGeneration.py
This script will create a CSV file named weather_data.csv containing synthetic weather data for 30 days.

Step 2: Map Weather Data

To visualize the weather data, run the WeatherMapping.py script:

bash
Always show details

Copy code
python WeatherMapping.py
This script will load the generated CSV file and create a side-by-side bar chart showing temperature and humidity trends.

Example
To generate weather data and create the visualization, use the following commands:

bash
Always show details

Copy code
python WeatherGeneration.py
python WeatherMapping.py

License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.