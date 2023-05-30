import numpy as np
import pandas as pd

returns = 'pandas dataframe'

sorted_returns = np.sort(returns)

confidence_level = 0.95

var = -np.percentile(sorted_returns, (1 - confidence_level) * 100)

print("Historical VaR at", confidence_level * 100, "% confidence level:", var)

import numpy as np
import pandas as pd

returns = np.array([0.01, -0.02, 0.03, -0.01, 0.02, -0.01, -0.02, 0.01])  # Replace with your actual historical returns

sorted_returns = np.sort(returns)
confidence_level = 0.95

var = -np.percentile(sorted_returns, (1 - confidence_level) * 100)

print("Historical VaR at", confidence_level * 100, "% confidence level:", var)
