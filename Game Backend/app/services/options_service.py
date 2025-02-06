
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models.options import Options
import re

def extract_float(text):
    """Extracts the first float value from a string using regex."""
    match = re.search(r"[-+]?\d*\.\d+|\d+", text.replace(',', ''))
    return float(match.group()) if match else 0.0


def scrape_options_data(db: Session):
    url = "https://finance.yahoo.com/markets/options/most-active/?start=0&count=100"
    
    # Add headers to mimic a real browser
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": f"Failed to fetch data, status code : {response.status_code}"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    table_rows = soup.select("tbody tr")
    options_data = []
    
    for row in table_rows:
        columns = row.find_all("td")

        # DEBUG: Print raw column contents to verify order
        raw_data = [col.text.strip() for col in columns]
        print(f"Raw data for row: {raw_data}")


        if len(columns) < 5:
            continue
        
        option = Options(
            symbol=columns[0].text.strip(),
            name=columns[1].text.strip(),
            last_price=extract_float(columns[2].text.replace(',', '').strip()),
            change=extract_float(columns[3].text.replace(',', '').strip()),
            percent_change=extract_float(columns[4].text.replace('%', '').strip()),
            volume=extract_float(columns[5].text.replace(',', '').strip()) if len(columns) > 5 else None
        )
        db.merge(option)
        options_data.append(option)
    
    db.commit()
    return options_data