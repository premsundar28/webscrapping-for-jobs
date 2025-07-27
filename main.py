# This file is part of the webscrapping-for-jobs project.
# It contains the main script for scraping job listings from a website. 

from bs4 import BeautifulSoup # BeautifulSoup is used for parsing HTML and XML documents
import requests # requests is used to send HTTP requests and handle responses

URL = "https://remoteok.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.text, "html.parser") # Parse the page content with BeautifulSoup


print(soup.prettify()) # Print the parsed HTML in a readable format