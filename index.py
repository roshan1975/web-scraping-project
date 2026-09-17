from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

all_data = []
column_names = []

for i in range(1, 6):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    header = {"User-Agent": "Mozilla/5.0"}

    print(f"Scraping page: {i}")
    response = requests.get(url, headers=header)
    
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="table")
    if table is None:
        continue

    rows = table.find_all("tr")