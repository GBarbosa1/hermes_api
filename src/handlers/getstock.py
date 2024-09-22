import yfinance as yf

class GetStock():
    
    def __init__(self):
        self.stock = None
        self.info = None
        self.value = None
        self.pvp = None
        self.div = None

    def stock_fundamentals(self, symbol):
        self.stock = yf.Ticker(symbol)
        self.info = self.stock.info
        self.payload = {
            symbol:
            {
            "dividends" : self.info['dividendYield'],
            "previousClose": self.info['previousClose']
            }
            
        }