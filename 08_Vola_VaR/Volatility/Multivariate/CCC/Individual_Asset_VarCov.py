import pandas as pd
import numpy as np
import arch

# Step 1: Prepare your data
data = pd.read_csv('returns.csv', index_col='date', parse_dates=True)

# Step 2: Create an arch GARCH model object and fit the model
model = arch.arch_model(data, vol='Garch', p=1, q=1, dist='Normal')
results = model.fit()

# Step 3: Calculate the variance-covariance matrix
cov_matrix = results.conditional_covariance

# Step 4: Extract the variance-covariance of each asset
asset_names = data.columns
asset_covariances = {}
for i, asset_name in enumerate(asset_names):
    asset_covariances[asset_name] = cov_matrix[:, i, i]

# Step 5: Print the variance-covariance of each asset
for asset_name, covariance in asset_covariances.items():
    print(f"Asset: {asset_name}")
    print(f"Variance: {covariance}")
    print()
