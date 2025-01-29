import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models.stock import Stock

def scrape_stock_data(db: Session):
    url = "https://finance.yahoo.com/markets/stocks/most-active/"
    
    # Add headers to mimic a real browser
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")
    table_rows = soup.select("tbody tr")
    
    stocks = []
    
    for row in table_rows:
        columns = row.find_all("td")
        if len(columns) < 6:  # Ensure we have all required columns
            continue
        
        try:
            stock = Stock(
                symbol=columns[0].text.strip(),
                name=columns[1].text.strip(),
                price=(columns[2].text.replace(',', '').replace('--', '0')),
                change=(columns[3].text.replace(',', '').replace('--', '0')),
                percent_change=(columns[4].text.replace('%', '').replace(',', '').replace('--', '0')),
                volume=(columns[5].text.replace(',', '').replace('--', '0'))
            )

            db.merge(stock)  # Upsert: Merge new stock data into the database
            stocks.append(stock)
        
        except ValueError as e:
            print(f"Error parsing stock data: {e}")  # Log error but continue processing

    db.commit()  # Save changes
    return stocks  