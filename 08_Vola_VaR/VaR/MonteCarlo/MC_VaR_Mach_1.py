import numpy as np

def calculate_var(portfolio_values, confidence_level):
    sorted_values = np.sort(portfolio_values)
    index = int((1 - confidence_level) * len(sorted_values))
    var = sorted_values[index]
    return var

# Example usage
# Generate random samples using a normal distribution with mean 0 and standard deviation 1
mean = 0
std_dev = 1
num_samples = 10000
samples = np.random.normal(mean, std_dev, num_samples)

# Calculate portfolio values
initial_investment = 1000000
returns = 0.05  # Assumed portfolio returns
portfolio_values = initial_investment * (1 + returns) ** samples

# Calculate VaR at 95% confidence level
confidence_level = 0.95
var = calculate_var(portfolio_values, confidence_level)
print(f"VaR at {confidence_level * 100}% confidence level: {var}")
