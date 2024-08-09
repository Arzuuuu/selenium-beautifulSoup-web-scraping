# Web Scraping and Data Extraction Project

This project demonstrates web scraping and data extraction using Selenium and BeautifulSoup4.

## Site

The site used for scraping is [Books to Scrape](https://books.toscrape.com/index.html).

## Scripts

- **`project.py`**: Uses Selenium to navigate through pages on 'Books to Scrape' and saves the HTML of each product listing.
- **`collect.py`**: Processes the saved HTML files with BeautifulSoup to extract book titles, prices, and links, and saves the data into a CSV file.

# Requirements
Selenium
BeautifulSoup4
pandas
