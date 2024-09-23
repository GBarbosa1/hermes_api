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
            "dividend_yield":self.div
            }
        }