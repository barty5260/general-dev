import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame({
    'A': np.random.randint(0, 10, 5),
    'B': np.random.randint(0, 10, 5),
    'C': np.random.randint(0, 10, 5),
    'D': np.random.randint(0, 10, 5),
    'E': np.random.randint(0, 10, 5)
})

# Calculate the rolling mean of the A, B, and C rows using a window size of 3
window_size = 3
rolling_mean = df[['A', 'B', 'C']].rolling(window_size, min_periods=1, axis=0).mean()

# Add the rolling mean to the original dataframe in a new column named 'F'
df['F'] = rolling_mean.iloc[-1, :]

# Alternatively, you can assign the rolling mean to the 'F' column directly
df['F'] = df[['A', 'B', 'C']].rolling(window_size, min_periods=1, axis=0).mean().iloc[-1, :]

'axis=0 (default): specifies that the operation should be performed along the rows, i.e., vertically. For example, calculating the mean of a column or dropping a row.'
'axis=1: specifies that the operation should be performed along the columns, i.e., horizontally. For example, calculating the mean of a row or dropping a column.'