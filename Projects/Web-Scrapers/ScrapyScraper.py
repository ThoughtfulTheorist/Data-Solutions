import scrapy
import csv
import os

import scrapy
import csv

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//span[@class='text']/text()").extract()
        
        # Check if any occurrences were found
        if quotes:
            self.logger.info(f"Found quotes: {quotes}")
        else:
            quotes = ["No quotes found"]
            self.logger.info("No quotes found on the page")
        
        # Save found quotes to CSV
        self.save_to_csv(quotes, 'quotes_found.csv')
        
        # Logging the completion
        self.logger.info("Data has been saved to quotes_found.csv")

    def save_to_csv(self, data, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote'])
            for item in data:
                writer.writerow([item])
