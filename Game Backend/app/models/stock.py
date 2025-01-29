from sqlalchemy import Column, String, Float
from app.database import Base

class Stock(Base):
    __tablename__ = "stocks"
    symbol = Column(String, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    change = Column(String)
    percent_change = Column(String)
    volume = Column(String)