from fastapi import FastAPI
from handlers.getstock import GetStock
import yfinance as yf

app = FastAPI()
stock = GetStock()

@app.get("/stock/{symbol}")
async def get_symbol(symbol : str):
    stock.stock_fundamentals(symbol)
    return stock.payload