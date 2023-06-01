import numpy as np
import pandas as pd
from scipy.stats import norm

# Define portfolio weights and historical returns
weights = np.array([0.3, 0.4, 0.3])  # Example weights
returns = pd.read_csv('returns.csv')  # Replace 'returns.csv' with your own historical return data

# Calculate log returns
log_returns = np.log(1 + returns.pct_change()).dropna()

# Calculate EWMA covariance matrix
lambda_param = 0.94  # Example decay factor, adjust as needed
cov_matrix = log_returns.cov()
ewma_cov_matrix = cov_matrix.ewm(alpha=lambda_param).mean()

# Set confidence level and time horizon
confidence_level = 0.95  # Example confidence level
time_horizon = 1  # Example time horizon (e.g., 1 day)

# Create an empty list to store VaR values
var_history = []

# Iterate through historical returns
for _, row in log_returns.iterrows():
    # Calculate portfolio volatility
    portfolio_volatility = np.sqrt(np.dot(weights, np.dot(ewma_cov_matrix, weights.T)))
    
    # Calculate VaR for the given time horizon
    z_score = norm.ppf(1 - confidence_level)
    var = portfolio_volatility * z_score * np.sqrt(time_horizon)
    
    # Append VaR value to history
    var_history.append(var)

# Convert the list to a pandas Series or DataFrame if desired
var_history = pd.Series(var_history)

# Print or use var_history for further analysis or backtesting
print(var_history)
