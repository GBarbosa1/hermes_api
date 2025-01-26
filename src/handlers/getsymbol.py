import yfinance as yf
from datetime import datetime, timedelta

class getSymbol():
    
    def __init__(self):
        self.stock = None
        self.info = None
        self.value = None
        self.pvp = None
        self.div = None

    def stock_fundamentals(self, symbol):
        self.stock = yf.Ticker(symbol)
        self.info = self.stock.info
        self.payload =  self.stock.info
        self.symbol = self.stock.info['symbol']
        self.previousClose  = self.info['previousClose']
        self.trailingPe  = self.info['trailingPE']
        if 'dividendYield' in self.payload:
            self.div = self.payload['dividendYield']
        else:
            self.div = 0
        self.payload = {
            self.symbol:
            {
            "value":self.previousClose,
            "price_earnings":self.trailingPe,
            "dividend_yield":(self.div)*100
            }
        }
        
    def stock_price(self, symbol, start_date, end_date = None):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if end_date is None:
            end_date = start_date + timedelta(days=1)
        else:
            pass
        stock = yf.Ticker(symbol)
        self.payload = stock.history(start=start_date, end = end_date)
        stock_row = self.payload.iloc[0]

        self.payload = {
            "open": stock_row["Open"],
            "high": stock_row["High"],
            "low": stock_row["Low"],
            "close": stock_row["Close"],
            "volume": int(stock_row["Volume"]),
        }
