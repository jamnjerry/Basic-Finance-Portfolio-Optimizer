import pandas as pd
import yfinance as yf
from datetime import datetime

def fetch_price_data(tickers, start_date, end_date):
    """
    Fetches historical 'Adj Close' prices from Yahoo Finance
    for a list of tickers.
    """
    print(f"Fetching data for: {', '.join(tickers)}...")
    
    try:
        # Download data
        data = yf.download(tickers, start=start_date, end=end_date)
        print(data)
        
        # Select only the 'Adj Close' prices
        # If you only download one ticker, yf returns a different structure
        if len(tickers) == 1:
            prices = data[['Close']]
        else:
            prices = data['Close']
            
        # Drop any rows with all missing data
        prices = prices.dropna(how='all')
        
        print("Data fetched successfully.")
        return prices
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_daily_returns(prices_df):
    """
    Calculates daily percentage returns from a DataFrame of prices.
    """
    if prices_df is None:
        return None
        
    # .pct_change() calculates the percentage change between the current and prior row
    daily_returns = prices_df.pct_change()
    
    # The first row will be NaN (since there's no prior day), so we drop it
    daily_returns = daily_returns.dropna(how='all')
    
    return daily_returns

# --- This part lets you test the script directly ---
if __name__ == "__main__":
    
    # 1. Define your inputs
    # Let's add a market index (S&P 500) right away
    asset_tickers = ['AAPL', 'MSFT', 'GOOG', 'JPM']
    market_index = '^GSPC' 
    all_tickers = asset_tickers + [market_index]
    
    start_date = "2020-01-01"
    end_date = datetime.now().strftime('%Y-%m-%d') # Use today's date as end

    # 2. Fetch prices
    print("--- Fetching Prices ---")
    prices = fetch_price_data(all_tickers, start_date, end_date)
    
    if prices is not None:
        print("\n--- Sample Prices (Last 5 days) ---")
        print(prices.tail())

        # 3. Calculate returns
        print("\n--- Calculating Daily Returns ---")
        returns = calculate_daily_returns(prices)
        
        if returns is not None:
            print("\n--- Sample Returns (Last 5 days) ---")
            print(returns.tail())