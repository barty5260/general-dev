import scipy.stats as stats
import numpy as np
import pandas as pd

# Create a sample DataFrame
data = {
    'Returns': [0.02, 0.01, -0.03, 0.015, -0.01, 0.02, -0.015, 0.03, -0.02, 0.025]
}
df = pd.DataFrame(data)

# Assign the column name
column_name = 'Returns'

# Retrieve the desired column values
retVec = df[column_name].values

# Estimate mean and std
retMean = np.mean(retVec)
retStd = np.std(retVec)

p = 0.01  # VaR level
Nmc = 10000000

# Monte Carlo simulation using normal returns
retMC = np.random.normal(loc=retMean, scale=retStd, size=Nmc)

# Portfolio values
port1Day = (1 + retMC) * 100.
PStarMC = np.percentile(port1Day, 100. * p)
VaRMC = 100. - PStarMC

RStar = stats.norm.ppf(p, loc=retMean, scale=retStd)
VaR = 100. - (RStar + 1.) * 100.

fmt = "%6.4f %6.4f"
print(fmt % (VaRMC, VaR))

# In the provided code snippet, VaRMC represents the Value at Risk (VaR) calculated using the Monte Carlo simulation approach, while VaR represents the VaR calculated using the parametric approach.

# VaRMC: This is the VaR estimated using the Monte Carlo simulation approach. The code generates random samples from a normal distribution based on the mean (retMean) and standard deviation (retStd) of the provided returns (retVec). The simulated returns are used to calculate portfolio values (port1Day), and the np.percentile function is applied to obtain the desired quantile (100 * p). The calculated percentile is subtracted from 100 to obtain the VaR value (VaRMC).

# VaR: This represents the VaR calculated using the parametric approach. It uses the inverse cumulative distribution function (stats.norm.ppf) from the scipy.stats module to determine the quantile corresponding to the desired probability (p). The loc parameter represents the mean return (retMean), and the scale parameter represents the standard deviation of returns (retStd). The obtained quantile is then subtracted from 100 to obtain the VaR value (VaR).

# Both VaRMC and VaR provide estimates of the potential loss (as a percentage of the initial investment) at a specified confidence level (p). VaRMC is obtained through the Monte Carlo simulation, while VaR is derived from the assumed normal distribution using the parametric approach.