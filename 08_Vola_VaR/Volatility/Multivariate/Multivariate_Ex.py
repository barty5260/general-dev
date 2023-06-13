import numpy as np
from scipy.stats import norm

# Define the parameters
confidence_level = 0.95  # 95% confidence level
investment = 10000      # Initial investment amount
holding_period = 30     # Number of days in the holding period

# Define the portfolio weights
weights = [0.4, 0.3, 0.3]  # Example weights for a portfolio of 3 assets

# Collect historical returns data for each asset
returns_asset1 = [0.02, -0.03, 0.05, -0.01, 0.01, -0.02, 0.03, -0.02, 0.04, -0.02]
returns_asset2 = [0.01, -0.02, 0.03, -0.02, 0.04, -0.02, 0.01, -0.03, 0.02, -0.01]
returns_asset3 = [-0.01, 0.03, -0.02, 0.04, -0.01, 0.02, -0.03, 0.02, -0.02, 0.03]

# Combine returns into a matrix
returns_matrix = np.array([returns_asset1, returns_asset2, returns_asset3])

# Calculate the mean returns of each asset
mean_returns = np.mean(returns_matrix, axis=1)

# Calculate the covariance matrix of returns
cov_matrix = np.cov(returns_matrix)

# Calculate the portfolio return
portfolio_return = np.dot(weights, mean_returns)

# Calculate the portfolio standard deviation
portfolio_std_dev = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))

# Calculate the z-score for the chosen confidence level
z_score = norm.ppf(1 - confidence_level)

# Calculate the VaR
var = investment * (portfolio_return - z_score * portfolio_std_dev * np.sqrt(holding_period))

# Print the VaR result
print(f"The multivariate VaR at a {confidence_level*100}% confidence level over a {holding_period}-day period is: {var:.2f}")
