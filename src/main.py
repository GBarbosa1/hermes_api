from fastapi import FastAPI
from handlers.getsymbol import getSymbol
import yfinance as yf

app = FastAPI()
stock = getSymbol()

@app.get("/stock/{symbol}")
async def get_symbol_fundamentals(symbol : str):
    stock.stock_fundamentals(symbol)
    return stock.payload