# metrics_calculator.py
import sys
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

def calculate_covariance_matrix(returns_df):
    """
    Calculates the covariance matrix of asset returns.
    """
    if returns_df is None:
        return None

    return returns_df.cov()

def calculate_asset_beta(asset_returns, market_returns):
    """
    Calculates the beta of each asset relative to the market index.
    """
    X = market_returns

    Y = asset_returns

    X = sm.add_constant(X)  # Adds a constant term to the predictor

    model = sm.OLS(Y, X).fit()

    print(model.summary())
    
    beta = model.params[1]

    return beta

# metrics_calculator.py (continued)

if __name__ == "__main__":
    
    # 1. Fetch and process data (using Week 1 functions)
    print("--- 1. Fetching and Calculating Returns ---")
    prices = fetch_price_data(ALL_TICKERS, START_DATE, datetime.now().strftime('%Y-%m-%d'))
    returns = calculate_daily_returns(prices)
    
    # Drop the market index from the asset returns DataFrame for the matrix calc
    # but keep it handy for the beta calculation.
    asset_returns = returns.drop(columns=[MARKET_TICKER])
    market_returns = returns[MARKET_TICKER]
    
    # ----------------------------------------------------------------------
    
    # 2. Calculate the Covariance Matrix (Input for optimization)
    print("\n--- 2. Covariance Matrix Calculation ---")
    cov_matrix = calculate_covariance_matrix(asset_returns)
    print(cov_matrix.round(8)) # Rounding for cleaner output
    
    # ----------------------------------------------------------------------
    
    # 3. Calculate all Asset Betas (Input for optimization constraints)
    print("\n--- 3. Individual Asset Betas ---")
    asset_betas = {}
    
    # Loop through each asset to calculate its beta against the S&P 500
    for ticker in ASSETS:
        beta = calculate_asset_beta(returns[ticker], market_returns)
        asset_betas[ticker] = beta
        print(f"Beta for {ticker}: {beta:.4f}")
        
    # Store the betas as a Pandas Series for easy access in Week 3
    betas_series = pd.Series(asset_betas)
    
    print("\nWeek 2 Complete: Covariance Matrix and Betas are ready for optimization.")

