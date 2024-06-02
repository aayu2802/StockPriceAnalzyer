import yfinance as yf
from datetime import datetime, timedelta
import mplfinance as mpf


class StockPriceAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, start=datetime.today() - timedelta(days=182), end=datetime.today())

    def plot_candlestick(self):
        mpf.plot(self.data, type='candle', volume=True, style='yahoo')

analyzer = StockPriceAnalyzer('RELIANCE.NS')
analyzer.plot_candlestick()