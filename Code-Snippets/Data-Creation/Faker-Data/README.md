# Product Creation

This project provides a Python script named `ProductCreation.py` that generates a CSV file with random product data using the `faker` library. The script creates 7,500 unique product entries, each with details such as SKU, name, description, cost, price, and dates related to the product's addition and last update.

## Features

- **Unique Product SKUs:** Generates unique SKUs for each product.
- **Random Product Names and Descriptions:** Uses `faker` to create believable product names and descriptions.
- **Dynamic Pricing:** Simulates pricing changes over time by assigning previous and current prices.
- **Date Handling:** Each product has a 'Date Added' and a 'Last Date Updated' to track changes.

## Requirements

- Python 3.x
- Pandas: `pip install pandas`
- Faker: `pip install Faker`

## Usage

Run the script using Python:

python ProductCreation.py

## Contact

If you have any questions or suggestions for improvements, please feel free to raise an issue in the GitHub repository where this project is hosted.