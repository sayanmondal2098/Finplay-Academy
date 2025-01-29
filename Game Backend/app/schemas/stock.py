from pydantic import BaseModel

class StockBase(BaseModel):
    symbol: str
    name: str
    price: str
    change: str
    percent_change: str
    volume: str