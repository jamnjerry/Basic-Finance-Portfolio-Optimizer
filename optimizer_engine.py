#opmitizer_engine.py

from scipy.optimize import minimize
from metrics_calculator import betas_series, cov_matrix
from data_manager import asset_tickers, market_index, all_tickers, start_date # Import Wk 1 variables

import numpy as np

def portfolio_stdev(weights, covariance_matrix):
    """
    Calculate the portfolio risk given asset weights and covariance matrix.
    """
    stdev = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

    return stdev

def portfolio_weights_sum(weights):
    """
    Ensure that the sum of portfolio weights equals 1.
    """
    return np.sum(weights) - 1

def beta_constraint(weights, betas, target_beta):
    """
    Calculate the difference between portfolio beta and target beta 
    given asset weights, asset returns, and market returns.
    """
    beta = np.dot(weights, betas)
    
    return target_beta - beta

def find_optimal_weights(covariance_matrix, betas, target_beta):
    """
    Find the optimal asset weights that minimize portfolio risk 
    while achieving the target beta.
    """
    # Initial guess: equal weights
    num_assets = len(betas)
    initial_weights = np.array([1.0 / num_assets] * num_assets)

    # Constraints: weights sum to 1 and portfolio beta equals target beta
    constraints = (
        {'type': 'eq', 'fun': portfolio_weights_sum},
        {'type': 'eq', 'fun': beta_constraint, 'args': (betas, target_beta)}
    )

    # Bounds: weights between 0 and 1 (no short selling)
    bounds = tuple((0, 1) for _ in range(num_assets))

    # Optimize
    result = minimize(portfolio_stdev,
                      x0=initial_weights,
                      args=(covariance_matrix,),
                      method='SLSQP',
                      bounds=bounds,
                      constraints=constraints)
    
    weights = dict(zip(asset_tickers, [round(float(i), 2) for i in result.x]))

    if result.success:
        return weights
    else:
        raise ValueError("Optimization failed: " + result.message)
    
if __name__ == "__main__":
    # Example usage
    target_beta = 1.1
    
    optimal_weights = find_optimal_weights(cov_matrix, betas_series.values, target_beta)

    result = f"Optimal Weights for Target Beta of {target_beta:.2f}:\n{optimal_weights}"
    print(result)
