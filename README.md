# eBay Automated Price Tracker 

A Python-based web scraping tool that tracks and records the prices of items listed on eBay. The tool scrapes prices from a specific eBay search results page, calculates the average price, removes outliers, and saves both individual prices and the average to a CSV file along with the current date.

![Capture1](https://github.com/user-attachments/assets/7ddb97ee-88ef-4d2e-b507-173e9cfd4c88)
![Capture2](https://github.com/user-attachments/assets/3edb2522-6081-4957-92c0-c68037988cf3)


## Features
  -	Scraping eBay Prices: Retrieves the prices of items from an eBay search results page using BeautifulSoup.
  -	Outlier Removal: Cleans the data by removing prices that deviate significantly from the average.
  -	Average Price Calculation: Automatically computes the average price of all valid prices listed on the page.
  -	CSV Storage: Records individual item prices, the calculated average price, and the date in a CSV file.
  -	Error Handling: Skips prices that are in a range format (e.g., "$5.00 to $10.00") and logs any conversion issues.

## Prerequisites
  -	Python 3.x
  -	Libraries:
    +	requests: For fetching the HTML content of the eBay search page.
    +	BeautifulSoup4: For parsing the HTML and extracting relevant data.
    +	numpy: For handling array operations and statistical calculations.
    +	csv: For writing data to a CSV file.

### Install the required libraries using the following command:
`pip install requests beautifulsoup4 numpy`

## Usage
1. Clone the repository:
  -  `git clone https://github.com/your-username/ebay-price-tracker.git`
   - `cd ebay-price-tracker`

2. Configure the eBay search URL: In the script, replace the LINK variable with your desired eBay search URL.
    Example: LINK = "https://www.ebay.ca/sch/i.html?_nkw=batmobile&_sacat=0"

3. Run the script: Execute the following command to run the price tracker:
    `python priceTracker.py`

4. CSV Output: The script generates or appends to a prices.csv file, where it stores:
    - Date
    - Individual prices
    - The average price for that batch of items

   Example CSV output:
     September-11-2024, 8.99, 45.67
     September-11-2024, 17.49, 45.67
     September-11-2024, 81.37, 45.67
     September-11-2024, 29.99, 45.67

## How It Works
    1.	Web Scraping: The script sends an HTTP request to eBay, retrieves the HTML content of the search results page, and parses it using BeautifulSoup.
    2.	Data Extraction: Prices are extracted by locating the relevant HTML tags. The script skips price ranges (e.g., "$5.00 to $10.00") to avoid inaccurate averages.
    3.	Outlier Removal: Prices that fall too far from the mean (beyond 2 standard deviations) are filtered out to produce a cleaner dataset.
    4.	Storage: All valid prices, along with the average price and the current date, are saved to a CSV file for record-keeping.

## Limitations
    Single Page Scrape: The script currently only scrapes a single page of search results. To scrape multiple pages, you would need to modify the script to handle pagination.
    Currency Support: The script only processes prices in dollars (removes $ and C symbols). It does not handle other currencies or currency conversion.

## Future Improvements
   - Add multi-page scraping for a more comprehensive price analysis.
   - Implement support for different currencies and currency conversion.
   - Add command-line arguments for dynamic search URLs and output file names.

## License
  This project is licensed under the MIT License.
