import requests
from bs4 import BeautifulSoup
import csv

def fetch_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Search for quotes on the webpage
    quotes = []
    for quote in soup.find_all('span', class_='text'):
        quotes.append(quote.get_text())

    # Check if any occurrences were found
    if not quotes:
        quotes = ["No quotes found"]

    return quotes

def save_quotes_to_csv(quotes, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote'])
        for quote in quotes:
            writer.writerow([quote])

# URL to scrape
url = 'http://quotes.toscrape.com/'
filename = 'quotes_found.csv'

# Fetch quotes
quotes = fetch_quotes(url)

# Save quotes to CSV
save_quotes_to_csv(quotes, filename)

print("Quotes have been saved to", filename)