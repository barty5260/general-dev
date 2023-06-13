import numpy as np
from scipy.stats import norm

returns = [0.02, 0.01, -0.03, 0.015, -0.01]

mean_return = np.mean(returns)
std_dev = np.std(returns)

confidence_level = 0.95
time_horizon = 1

z_score = norm.ppf(confidence_level)

var = mean_return - z_score * std_dev * np.sqrt(time_horizon)

print("Parametric VaR at {}% confidence level: {:.2%}".format(confidence_level * 100, var))

# These three vars are very similar, take a deeper look and choose. MC_VaR_2 also calculates parametric approach.