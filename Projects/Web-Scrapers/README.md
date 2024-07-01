# WebScraper
 A simple SEO WebScraper that will be built upon over time.

## BeautifulSoupScraper.py
This project is a simple web scraper built using BeautifulSoup to extract quotes from the website `quotes.toscrape.com` and save them into a CSV file. The scraper crawls the website, extracts quotes, and stores them in a file named `quotes_found.csv`.

## Requirements

- Python 3.6+
- BeautifulSoup 4
- Requests

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/ThoughtfulTheorist/WebScraper.git
   cd quotes-bs4-scraper
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   ```sh
   pip install requests beautifulsoup4
   ```

## Project Structure

```
quotes-bs4-scraper/
├── scrape_quotes.py
└── README.md
```

## Usage

1. **Navigate to the Project Directory**

   ```sh
   cd quotes-bs4-scraper
   ```

2. **Run the Scraper**

   ```sh
   python scrape_quotes.py
   ```

   This will start the scraper, which will crawl the `quotes.toscrape.com` website, extract quotes, and save them into a file named `quotes_found.csv` located in the same directory.

## Modifying the Scraper

If you need to modify the scraper to extract different data or target a different website, you can edit the `scrape_quotes.py` file.

### Example: Modify the Start URL

Open `scrape_quotes.py` and change the `url` variable:

```python
url = 'http://quotes.toscrape.com/'
```

You can set it to any other URL you want to scrape:

```python
url = 'http://otherwebsite.com/'
```

### Example: Modify the HTML Parsing

To extract different data, modify the BeautifulSoup parsing logic inside the `fetch_quotes` function:

```python
quotes = []
for quote in soup.find_all('span', class_='text'):
    quotes.append(quote.get_text())
```

Change the HTML tags and attributes to target the specific data you want to scrape.

## Output

The output CSV file, `quotes_found.csv`, will be saved in the project directory. By default, it is set to save in the same directory where the script is run.

## Troubleshooting

- Ensure you have the correct versions of Python and required libraries installed.
- Verify that the target website allows scraping and does not block your requests.
- Check the script's output for any errors or warnings.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Quotes to Scrape](http://quotes.toscrape.com/) - A practice website for web scraping




## ScrapyScraper.py
Currently this project is a simple web scraper built using Scrapy to extract quotes from the website `quotes.toscrape.com` and save them into a CSV file. The spider crawls the website, extracts quotes, and stores them in a file named `quotes_found.csv`.

## Requirements

- Python 3.6+
- Scrapy 2.11.2

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/ThoughtfulTheorist/WebScraper.git
   cd quotes-scraper
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   ```sh
   pip install scrapy
   ```

## Project Structure

```
quotes-scraper/
├── seo_project/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── ScrapyScraper.py
└── scrapy.cfg
```

## Usage

1. **Navigate to the Project Directory**

   ```sh
   cd quotes-scraper
   ```

2. **Run the Spider**

   ```sh
   scrapy crawl quotes
   ```

   This will start the spider, which will crawl the `quotes.toscrape.com` website, extract quotes, and save them into a file named `quotes_found.csv` located on your desktop (`C:/Users/YourUserName/YourFilePath/quotes_found.csv`).

## Modifying the Spider

If you need to modify the spider to scrape different data or a different website, you can edit the `quotes_spider.py` file located in the `seo_project/spiders/` directory.

### Example: Modify the Start URL

Open `quotes_spider.py` and change the `start_urls` list:

```python
start_urls = ['http://quotes.toscrape.com/']
```

You can add multiple URLs if needed:

```python
start_urls = [
    'http://quotes.toscrape.com/',
    'http://otherwebsite.com/'
]
```

### Example: Modify the XPath Expression

To extract different data, modify the XPath expression inside the `parse` method:

```python
quotes = response.xpath("//span[@class='text']/text()").extract()
```

Change the expression to target the specific data you want to scrape.

## Output

The output CSV file, `quotes_found.csv`, will be saved to the specified path. By default, it is set to `C:/Users/Kyle/Desktop/quotes_found.csv`.

## Troubleshooting

- Ensure you have the correct versions of Python and Scrapy installed.
- Verify that the `robots.txt` rules of the target website allow crawling.
- Check the Scrapy logs for any errors or warnings.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scrapy Documentation](https://docs.scrapy.org/)
- [Quotes to Scrape](http://quotes.toscrape.com/) - A practice website for web scraping
