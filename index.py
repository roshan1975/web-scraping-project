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
    print(f"Scraping page-2: {i}")
    response = requests.get(url, headers=header)
    
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="table")
    if table is None:
        continue

    rows = table.find_all("tr")
    
    if not column_names:
        header_row = rows[0].find_all(["th", "td"])
        column_names = [col.get_text(strip=True) for col in header_row]

    for row in rows[1:]:
        cols = row.find_all(["th", "td"])
        row_data = [col.get_text(strip=True) for col in cols]

        if row_data:
            all_data.append(row_data)
            
df = pd.DataFrame(all_data, columns=column_names)
folder = os.path.join(os.path.expanduser("~"), "Desktop")
os.makedirs(folder, exist_ok=True)
save_path = os.path.join(folder, "Hockey_Teams.csv")

df.to_csv(save_path, index=False)

print(f"Total data scraped: {len(df)}")
print(f"Saved to {save_path}")
