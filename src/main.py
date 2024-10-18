from fastapi import FastAPI
from handlers.getsymbol import getSymbol
from infraestructure.bcb_api import getBcbData
import yfinance as yf

app = FastAPI()
stock = getSymbol()
bcb = getBcbData()

@app.get("/stock/{symbol}")
async def get_symbol_fundamentals(symbol : str):
    stock.stock_fundamentals(symbol)
    return stock.payload

@app.get("/actual_brazilian_interest_rate/")
async def actual_brazilian_interest_rate():
    bcb.get_brazil_actual_selic()
    return bcb.payload