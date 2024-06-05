import yfinance as yf
from datetime import datetime, timedelta
import mplfinance as mpf
yf.pdr_override()
stock = "TATAMOTORS.NS"
interval = "1m"
class StockPriceAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker,start=datetime.now() - timedelta(days=1), end=datetime.now(), interval=interval)
    def plot_candlestick(self):
        mpf.plot(self.data, type='candle', volume=True, style='yahoo')
data = yf.download(stock, start=datetime.now() - timedelta(days=1), end=datetime.now(), interval=interval)
print(data)
analyzer = StockPriceAnalyzer(stock)
analyzer.plot_candlestick()