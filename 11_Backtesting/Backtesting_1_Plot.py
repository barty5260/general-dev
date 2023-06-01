import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = 0
var_values = 0
returns = 0
exceedances = 0
threshold = 0

# Step 7: Visualize the results
fig, ax = plt.subplots(2, 1, figsize=(12, 8))

# Plot VaR values
ax[0].plot(dates[1:], var_values[1:], label='VaR')
ax[0].set_ylabel('VaR')
ax[0].legend()

# Plot returns and exceedances
ax[1].plot(dates[1:], returns, label='Returns')
ax[1].plot(dates[1:], exceedances.astype(int) * threshold, 'ro', label='Exceedances')
ax[1].axhline(threshold, color='r', linestyle='--', label='Threshold')
ax[1].set_ylabel('Returns / Exceedances')
ax[1].legend()

plt.xlabel('Date')
plt.show()
