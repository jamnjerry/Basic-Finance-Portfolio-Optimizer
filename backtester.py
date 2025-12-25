from alpaca.trading.client import TradingClient
import alpaca_trade_api as tradeapi
import os
import pandas as pd
from optimizer_engine import find_optimal_weights
from metrics_calculator import betas_series, cov_matrix

target_beta = 1.1
weights = find_optimal_weights(cov_matrix, betas_series.values, target_beta)

key = os.getenv('APCA_API_KEY_ID')
secret = os.getenv('APCA_API_SECRET_KEY')

trading_client = TradingClient(key, secret,paper=True)
api = tradeapi.REST(key, secret, base_url='https://paper-api.alpaca.markets')

account = trading_client.get_account()

total_investment = account.cash


def backtest_portfolio(weights, total_investment):
    """
    Simulate a portfolio allocation based on optimal weights.
    """

    allocation = {ticker: round(weight * total_investment, 2) for ticker, weight in weights.items()}

    tickers = list(weights.keys())
    start_date = "2022-01-01"
    end_date = "2023-01-01"
    
    # 2. Fetch Historical Data from Alpaca
    # timeframe='1Day' gets daily closing prices
    data = api.get_bars(tickers, '1Day', start=start_date, end=end_date).df
    
    # Pivot data so columns are tickers and rows are dates
    prices = data.pivot(columns='symbol', values='close')
    
    # 3. Calculate Returns
    daily_returns = prices.pct_change().dropna()
    
    # 4. Apply Weights
    # weights_dict looks like: {'AAPL': 0.4, 'MSFT': 0.6}
    weights_series = pd.Series(weights)
    
    # Calculate daily portfolio return: (Returns * Weights).sum(axis=1)
    portfolio_daily_returns = daily_returns.dot(weights_series)
    
    # 5. Calculate Cumulative Growth (Starting with $1)
    cumulative_growth = (1 + portfolio_daily_returns).cumprod()[-1]
    
    return cumulative_growth


print(backtest_portfolio(weights, float(total_investment)))