import pandas as pd
import numpy as np

# Generate sample price data
np.random.seed(0)
prices = np.random.rand(100) * 100  # Random price values between 0 and 100

# Create a DataFrame with price data
df = pd.DataFrame({'Price': prices})

# Calculate log returns
df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))

# Calculate EWMA volatility
window_size = 10  # Adjust the window size as desired
lambda_param = 0.94  # Adjust the lambda (decay factor) as desired

# Calculate the weights using lambda
weights = np.power(lambda_param, np.arange(window_size-1, -1, -1))

# Assign the weights to log returns
df['Weighted_Log_Return'] = df['Log_Return'].rolling(window_size).apply(lambda x: np.dot(x, weights[::-1]))

# Calculate the squared weighted log returns
df['Squared_Weighted_Log_Return'] = df['Weighted_Log_Return']**2

# Calculate the EWMA volatility estimate
ewma_volatility = np.sqrt(df['Squared_Weighted_Log_Return'].rolling(window_size).sum() / window_size)

# Create a column for EWMA Volatility in the DataFrame
df['EWMA_Volatility'] = ewma_volatility

# Print the DataFrame with volatility
print(df)
