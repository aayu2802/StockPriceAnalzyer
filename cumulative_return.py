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

    def calculate_cumulative_returns(self):
        cumulative_returns = (1 + self.calculate_daily_returns()).cumprod()
        return cumulative_returns


    def plot_cumulative_returns(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.calculate_cumulative_returns())
        plt.title(f'{self.ticker} Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Return (%)')
        plt.show()
analyzer = StockPriceAnalyzer('RELIANCE.NS')
print(analyzer.calculate_cumulative_returns())
analyzer.plot_cumulative_returns()