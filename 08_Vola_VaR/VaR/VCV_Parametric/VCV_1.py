import numpy as np
from scipy.stats import norm

def calculate_var(returns, confidence_level):
    # Calculate the mean and standard deviation of returns
    mean_return = np.mean(returns)
    std_dev = np.std(returns)
    
    # Calculate the quantile for the desired confidence level
    z_score = norm.ppf(1 - confidence_level)
    
    # VaR as a positive loss: If you define VaR as a positive value representing a loss magnitude
    var = mean_return + z_score * std_dev
    
    return var

# Example usage
returns = [0.02, -0.03, 0.01, 0.04, -0.02, -0.01, 0.03, -0.02, 0.01, -0.01]
confidence_level = 0.95

var = calculate_var(returns, confidence_level)
print(f"The VaR at {confidence_level} confidence level is: {var}")
