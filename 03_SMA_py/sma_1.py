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


# Merge the dataframes
merged_df = pd.merge(df_main, df_lag1, on='ID')
merged_df = pd.merge(merged_df, df_lag2, on='ID')

# Calculate the moving average
merged_df['moving_avg'] = merged_df[['F', 'F_lag1', 'F_lag2']].rolling(window=3).mean()

# Keep only ID and moving_avg columns
merged_df = merged_df[['ID', 'moving_avg']]

merged_df