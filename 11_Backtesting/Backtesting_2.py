import numpy as np
import pandas as pd
from scipy.stats import chi2

# Step 2: Load the historical VaR data and portfolio values
var_data = pd.read_csv('var_history.csv')
portfolio_data = pd.read_csv('portfolio_values.csv')

var_data['Date'] = pd.to_datetime(var_data['Date'])
portfolio_data['Date'] = pd.to_datetime(portfolio_data['Date'])

data = pd.merge(var_data, portfolio_data, on='Date')

# Step 3: Calculate portfolio losses or gains
data['Portfolio Returns'] = data['Portfolio Value'].pct_change()
data.dropna(inplace=True)

# Step 4: Define the backtesting function
def var_backtest(data, alpha=0.05):
    data.sort_values(by='VaR', ascending=False, inplace=True)
    threshold = data['VaR'].quantile(1 - alpha)
    exceedances = data[data['Portfolio Returns'] < threshold]
    proportion = len(exceedances) / len(data)
    failures = len(exceedances)
    successes = len(data) - failures
    test_statistic = -2 * (failures * np.log((1 - proportion) / (1 - alpha)) + successes * np.log(proportion / alpha))
    p_value = 1 - chi2.cdf(test_statistic, 1)
    return threshold, proportion, test_statistic, p_value

# Step 5: Call the backtesting function
threshold, proportion, test_statistic, p_value = var_backtest(data)

# Print the backtesting results
print("Backtesting Results:")
print(f"VaR threshold: {threshold}")
print(f"Proportion of exceedances: {proportion}")
print(f"Test statistic: {test_statistic}")
print(f"p-value: {p_value}")
