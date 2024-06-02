import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class StockPriceAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, start=datetime.today() - timedelta(days=365), end=datetime.today())
    def get_stock_data(self):
        return self.data
    def plot_stock_price(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Close'])
        plt.title(f'{self.ticker} Stock Price')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.show()

analyzer = StockPriceAnalyzer('RELIANCE.NS')
print(analyzer.get_stock_data())
analyzer.plot_stock_price()