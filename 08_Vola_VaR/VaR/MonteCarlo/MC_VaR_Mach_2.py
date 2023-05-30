import numpy as np

# Define your portfolio or investment returns
returns = [0.01, -0.02, 0.015, 0.025, -0.01, -0.005, 0.02, -0.015, 0.012, -0.008, 0.03, -0.015,
           0.02, -0.025, 0.015, 0.01, -0.005, 0.02, -0.01, 0.025]

# Define the number of simulations and time horizon
num_simulations = 100000
time_horizon = 1  # In this example, we consider a one-day time horizon

# Define the confidence level for VaR calculation
confidence_level = 0.95  # 95% confidence level

# Calculate the portfolio value at the end of the time horizon for each simulation
portfolio_values = []
for _ in range(num_simulations):
    random_returns = np.random.choice(returns, time_horizon)
    portfolio_value = np.prod(1 + random_returns)
    portfolio_values.append(portfolio_value)

# Sort the portfolio values in ascending order
portfolio_values.sort()

# Calculate the VaR based on the confidence level
var_index = int((1 - confidence_level) * num_simulations)
var = -portfolio_values[var_index]

# Print the VaR result
print(f"The Value at Risk (VaR) at a {confidence_level*100}% confidence level is: {var:.2f}")