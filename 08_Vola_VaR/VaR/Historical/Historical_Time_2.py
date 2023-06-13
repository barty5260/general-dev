import numpy as np
import pandas as pd

returns = 'pandas dataframe'

sorted_returns = np.sort(returns)

confidence_level = 0.95

# Calculate the number of days for VaR
num_days_var = [10, 20, 250]  # Modify this list to include the desired number of days

for num_days in num_days_var:
    var = -np.percentile(sorted_returns, (1 - confidence_level) * 100) * np.sqrt(num_days)

    print("Historical VaR for", num_days, "days at", confidence_level * 100, "% confidence level:", var)
