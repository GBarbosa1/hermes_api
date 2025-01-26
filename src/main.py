from pydantic import BaseModel
from fastapi import FastAPI
from handlers.getsymbol import getSymbol
from infraestructure.bcb_api import getBcbData
import yfinance as yf

app = FastAPI()
stock = getSymbol()
bcb = getBcbData()

class DateSearch(BaseModel):
    start_date: str
    end_date: str = False

@app.get("/stock/fundamentals/{symbol}")
async def get_symbol_fundamentals(symbol : str):
    stock.stock_fundamentals(symbol)
    return stock.payload

@app.get("/stock/price/{symbol}")
async def get_symbol_price(symbol : str, start_date:DateSearch):
    stock.stock_price(symbol, start_date.start_date)
    return stock.payload

@app.get("/actual_brazilian_interest_rate/")
async def actual_brazilian_interest_rate():
    bcb.get_brazil_actual_selic()
    return bcb.payload

@app.get("/actual_brazilian_inflation/")
async def actual_brazilian_inflation():
    bcb.get_brazil_actual_inflation()
    return bcb.payload