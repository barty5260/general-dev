import numpy as np
import pandas as pd

# Define portfolio weights and historical returns
weights = np.array([0.3, 0.4, 0.3])  # Example weights
returns = pd.read_csv('returns.csv')  # Replace 'returns.csv' with your own historical return data

# Calculate log returns
log_returns = np.log(1 + returns.pct_change()).dropna()

# Calculate mean vector and covariance matrix
mean_vector = log_returns.mean().values
cov_matrix = log_returns.cov().values

# Set simulation parameters
num_simulations = 10000  # Number of simulations
num_assets = len(weights)  # Number of assets
initial_portfolio_value = 1000000  # Initial portfolio value

# Perform Monte Carlo simulation
simulation_results = np.zeros(num_simulations)
var_history = []  # List to store VaR values

# Set confidence level for VaR calculation
confidence_level = 0.95

for i in range(num_simulations):
    random_returns = np.random.multivariate_normal(mean_vector, cov_matrix, size=num_assets)
    portfolio_value = initial_portfolio_value * (1 + np.sum(weights * random_returns[-1, :]))
    simulation_results[i] = portfolio_value
    
    # Calculate VaR
    var_index = int((1 - confidence_level) * num_simulations)
    var = initial_portfolio_value - simulation_results[var_index]
    var_history.append(var)

# Sort simulation results in ascending order
simulation_results.sort()

# Rest of the code...

