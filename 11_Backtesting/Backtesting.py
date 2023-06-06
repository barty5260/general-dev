import pandas as pd

# Load your time series data into a pandas DataFrame
data = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with the actual file name or path

# Define your confidence level for VaR
confidence_level = 0.95  # Example confidence level of 95%

# Initialize variables
var_losses = []  # To track VaR violations (losses)
portfolio_value = 100000  # Initial portfolio value
portfolio_returns = []  # To track portfolio returns

# Perform the VaR backtest
for index, row in data.iterrows():
    # Get the return value and VaR for the current time period
    return_value = row['Return']
    var_value = row['VaR']
    
    # Check for VaR violation
    if return_value < -var_value:
        var_losses.append(return_value)
    
    # Update portfolio value and track returns
    portfolio_value *= (1 + return_value)
    portfolio_returns.append(portfolio_value)
    
# Calculate risk and performance metrics
var_losses_count = len(var_losses)
var_coverage = var_losses_count / len(data)  # VaR coverage ratio

# Print the results
print(f"VaR Coverage: {var_coverage:.4f}")
print(f"Number of VaR Violations: {var_losses_count}")
