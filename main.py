# This file is part of the webscrapping-for-jobs project.
# It contains the main script for scraping job listings from a website. 

from bs4 import BeautifulSoup # BeautifulSoup is used for parsing HTML and XML documents
import requests # requests is used to send HTTP requests and handle responses

URL = "https://www.moneycontrol.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, "html.parser") # Parse the page content with BeautifulSoup

title_div = soup.find('div', class_='stAcbx')

# Find both NSE and BSE tables
nse_table = soup.find("div", id="in_maNSE")
bse_table = soup.find("div", id="in_maBSE")

def extract_table_data(table, exchange_name):
    print(f"\n{exchange_name} Most Active Stocks:")
    print(f"{'Company':<25} {'Price':<10} {'Change':<10}")
    print("-" * 50)

    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            company = cols[0].text.strip()
            price = cols[1].text.strip()
            change = cols[2].text.strip()
            print(f"{company:<25} {price:<10} {change:<10}")

# Extract NSE data
extract_table_data(nse_table, "NSE")

# Extract BSE data
extract_table_data(bse_table, "BSE")