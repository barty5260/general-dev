import pandas as pd
import numpy as np

# Assuming you have a pandas DataFrame with a column of prices
# Create a sample DataFrame with price data
data = {'Date': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05'],
        'Price': [100.0, 102.0, 105.0, 99.0, 101.0]}
df = pd.DataFrame(data)

# Calculate log returns
df['Log_Return'] = df['Price'].pct_change().apply(lambda x: np.log(1 + x))

# Calculate EWMA volatility
window_size = 10  # Adjust the window size as desired
lambda_param = 0.94  # Adjust the lambda (decay factor) as desired
df['EWMA_Volatility'] = df['Log_Return'].ewm(alpha=lambda_param).std()

# Print the DataFrame with volatility
print(df)
