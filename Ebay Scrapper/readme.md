# eBay Price Range Scraper

This project is a basic web scraper that uses Selenium to search for products on eBay within a specified price range. A simple GUI built with Tkinter allows the user to input the search term, minimum price, and maximum price. The scraper then filters the results and saves the data to a CSV file.

## Features

- **GUI Input**: Enter search term, minimum price, and maximum price through a simple Tkinter interface.
- **Input Validation**: Ensures that the entered prices are numbers and that the search term is not empty.
- **Price Filtering**: Filters eBay search results based on the given price range.
- **Data Export**: Saves the filtered results (product title, price, and link) into a CSV file.

## Requirements

To run this project, you need the following Python packages:

- `selenium`
- `pandas`
- `tkinter` (comes with Python by default)
- `chromedriver` (Ensure it's compatible with your installed Chrome version)

You can install Selenium and pandas using pip:

```bash
pip install selenium pandas
```

Example
If you input the following:
```
Search Term: 3060Ti
Min Price: 1300
Max Price: 3200
```
The script will search for 3060Ti on eBay, filter results where the price is between 1300 and 3200, and save the results in a file named ebay_3060Ti_filtered.csv.


Notes
Make sure your Chrome browser is up-to-date to avoid compatibility issues with chromedriver.
This script is for educational purposes. Scraping websites like eBay should be done responsibly and in compliance with their terms of service.

License
This project is open-source and available under the MIT License.
