import numpy as np
from scipy.stats import norm

def calculate_var(returns, confidence_level):
    # Calculate portfolio or asset mean return and standard deviation
    mean_return = np.mean(returns)
    std_dev = np.std(returns)

    # Calculate the z-score corresponding to the confidence level
    z_score = norm.ppf(1 - confidence_level)

    # VaR as a negative loss: If you define VaR as the maximum potential loss, then the formula
    var = mean_return - z_score * std_dev

    return var

# Example usage
returns = [0.02, -0.03, 0.01, 0.04, -0.02, -0.01, 0.03, -0.02, 0.01, -0.01]  # Sample returns data
confidence_level = 0.95  # 95% confidence level

var = calculate_var(returns, confidence_level)
print(f"The Value at Risk (VaR) at a {confidence_level*100}% confidence level is: {var:.2%}")
