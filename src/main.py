from fastapi import FastAPI
from handlers.getstock import GetStock
import yfinance as yf

app = FastAPI()
stock = GetStock()

@app.get("/stock/{symbol}")
async def get_symbol(symbol : str):
    stock.stock_fundamentals(symbol)
    return stock.payload
    

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}