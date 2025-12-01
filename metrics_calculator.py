# metrics_calculator.py
import pandas as pd
import numpy as np
import statsmodels.api as sm
from data_manager import fetch_price_data, calculate_daily_returns # Import Wk 1 functions
from datetime import datetime

# Define assets and market index
ASSETS = ['AAPL', 'MSFT', 'GOOG', 'JPM']
MARKET_TICKER = '^GSPC' # S&P 500
ALL_TICKERS = ASSETS + [MARKET_TICKER]
START_DATE = "2020-01-01"

# --- Functions for Week 2 ---