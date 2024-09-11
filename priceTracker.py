from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=batmobile&_sacat=0"

def get_prices_by_link(link):
    # get source
    r = requests.get(link)
    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')
    # find all list items from search results
    search_results = page_parse.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

    item_prices = []

    for result in search_results:
        try:
            price_as_text = result.find("span", {"class": "s-item__price"}).text
            if "to" in price_as_text:  # skip ranges like "$5.00 to $10.00"
                continue
            price = float(price_as_text.replace("C", "").replace("$", "").replace(",", "").strip())
            item_prices.append(price)
        except:
            print(f"Price conversion error for: {price_as_text}")
            continue
    return item_prices

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_average(prices):
    return np.mean(prices)

def save_to_file(prices):
    avg_price = np.around(get_average(prices), 2)
    today = datetime.today().strftime("%B-%D-%Y")
    
    # Write each price to the CSV along with the average and date
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for price in prices:
            writer.writerow([today, np.around(price, 2), avg_price])

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    prices_without_outliers = remove_outliers(prices)
    print(f"Average price: {get_average(prices_without_outliers)}")
    save_to_file(prices)
