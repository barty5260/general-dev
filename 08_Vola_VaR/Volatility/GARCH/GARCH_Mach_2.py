import pandas as pd
from arch import arch_model

# Example time series data
returns = pd.Series([0.02, -0.01, 0.03, -0.02, 0.01, 0.02, -0.03, 0.02, -0.01, 0.02])

# Create a GARCH(1, 1) model
model = arch_model(returns, vol='Garch', p=1, q=1)

# Fit the GARCH model to the data
results = model.fit()

# Access the volatility estimates
volatility = results.conditional_volatility

print(volatility)
