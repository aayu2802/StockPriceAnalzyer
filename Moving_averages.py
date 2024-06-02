import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import mplfinance as mpf
import numpy as np

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

    def calculate_moving_averages(self, short_window, long_window):
        signals = pd.DataFrame(index=self.data.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = self.data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
        signals['long_mavg'] = self.data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

        signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

        return signals

    def plot_moving_averages(self, short_window, long_window):
        signals = self.calculate_moving_averages(short_window, long_window)
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Close'], label='Close Price')
        plt.plot(signals['short_mavg'], label='Short-term MA')
        plt.plot(signals['long_mavg'], label='Long-term MA')
        plt.plot(signals.index, signals['signal'] * self.data['Close'], label='Signals', linestyle='None', marker='^', color='g')
        plt.title(f'{self.ticker} Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price (Rs)')
        plt.legend(loc='best')
        plt.show()


# Example usage
analyzer = StockPriceAnalyzer('RELIANCE.NS')
analyzer.plot_moving_averages(20, 50)
