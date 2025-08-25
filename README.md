# Book Price Scraper (GBP → INR)

A Python script to **scrape book details** from [Books to Scrape](http://books.toscrape.com/).

## Features
- Extracts **book title**, **price**, and **rating**.
- Converts prices from **GBP (British Pounds) to INR (Indian Rupees)**.
- Saves the data in a **CSV file** (`products.csv`) with columns: `Product Name`, `Price (₹ INR)`, `Rating`.
- Prints the scraped data on the console for quick verification.

## Technologies Used
- Python
- `requests` for fetching web pages
- `BeautifulSoup` for parsing HTML
- `csv` module for saving data

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
