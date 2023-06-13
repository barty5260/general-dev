import numpy as np
import pandas as pd

# Creating a sample DataFrame
dates = pd.date_range(start='2023-01-01', end='2023-01-31', freq='B')
closing_prices = np.random.randint(100, 200, size=len(dates)).astype(float)
df = pd.DataFrame({'Date': dates, 'Close': closing_prices})

# Calculating historical volatility
returns = np.log(df['Close'] / df['Close'].shift(1))
historical_volatility = returns.std() * np.sqrt(252)

print('Historical Volatility:', historical_volatility)
