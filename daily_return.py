import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class StockPriceAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, start=datetime.today() - timedelta(days=182), end=datetime.today())


    def calculate_daily_returns(self):
        daily_returns = self.data['Close'].pct_change()
        return daily_returns
    def plot_daily_returns(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.calculate_daily_returns())
        plt.title(f'{self.ticker} Daily Returns')
        plt.xlabel('Date')
        plt.ylabel('Return (%)')
        plt.show()
analyzer = StockPriceAnalyzer('RELIANCE.NS')

print(analyzer.calculate_daily_returns())
analyzer.plot_daily_returns()