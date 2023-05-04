import pandas as pd
import numpy as np

# Create df_main
df_main = pd.DataFrame({
    'ID': ['A', 'B', 'C', 'D', 'E'],
    'F': np.random.randint(0, 10, 5)
})

# Create df_lag1
df_lag1 = pd.DataFrame({
    'ID': ['A', 'B', 'C', 'D', 'E'],
    'F_lag1': np.random.randint(0, 10, 5)
})

# Create df_lag2
df_lag2 = pd.DataFrame({
    'ID': ['A', 'B', 'C', 'D', 'E'],
    'F_lag2': np.random.randint(0, 10, 5)
})

# Calculate the moving average of column F in df_main using data from df_lag1 and df_lag2
df_ma = (df_main['F'] + df_lag1['F'] + df_lag2['F']) / 3

# Use rolling function to fill the missing values in the first two rows with data from df_main
df_ma = df_ma.rolling(3, min_periods=1).mean()

# Use fillna method to replace the remaining NaN values with data from df_main
df_ma.fillna(df_main['F'], inplace=True)
