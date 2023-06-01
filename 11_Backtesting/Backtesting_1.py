import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import the necessary libraries

# Step 2: Load your historical VaR data and portfolio values
var_data = pd.read_csv('var_data.csv')  # Assuming your data is in a CSV file
var_values = var_data['VaR'].values
portfolio_values = var_data['PortfolioValue'].values
dates = pd.to_datetime(var_data['Date'])  # Assuming you have a column called 'Date'

# Step 3: Determine the exceedances
threshold = -0.05  # Set your VaR threshold
exceedances = (portfolio_values[1:] < var_values[:-1] * portfolio_values[:-1]).astype(int)
exceedance_ratio = exceedances.mean()

# Step 4: Compute the p-value
p_value = np.mean(exceedances)

# Step 5: Evaluate the backtest
significance_level = 0.05
if p_value < significance_level:
    print("VaR model does not perform adequately.")
else:
    print("VaR model performs adequately.")

# Step 6: Visualize the results
fig, ax = plt.subplots(figsize=(12, 6))

# Plot VaR values and exceedances
ax.plot(dates[:-1], var_values[:-1] * portfolio_values[:-1], label='VaR * Portfolio Value')
ax.plot(dates[1:], portfolio_values[1:], label='Portfolio Value')
ax.plot(dates[1:], exceedances * portfolio_values[1:], 'ro', label='Exceedances')
ax.axhline(threshold * portfolio_values[0], color='r', linestyle='--', label='Threshold')
ax.set_ylabel('Value')
ax.legend()

plt.xlabel('Date')
plt.show()
