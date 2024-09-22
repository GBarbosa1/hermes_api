import yfinance as yf

alzr = yf.Ticker('ALZR11.SA')

info = alzr.info

print(info)