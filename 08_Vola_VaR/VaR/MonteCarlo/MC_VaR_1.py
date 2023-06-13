import numpy as np
from scipy.stats import norm
import numpy.matlib
from scipy.stats import uniform
import matplotlib.pyplot as plt
import math as m
import random as r
from scipy.stats import uniform

'https://medium.com/the-quant-journey/monte-carlo-methods-for-risk-management-var-estimation-in-python-1f42d4b0d574'

# General share info
S_0 = np.array([[100],[95],[50]])
sigma = np.array([[0.15],[0.2],[0.3]])
corr_mat = np.array([[1, 0.2, 0.4],[0.2, 1, 0.8],[0.4, 0.8, 1]])
L = np.linalg.cholesky(corr_mat)
r = 0.1
T = 1

np.random.seed(0)
t_simulations = 10000
alpha = 0.05
# current portfolio value
portval_current = np.sum(S_0)

def terminal_shareprice(S_0, risk_free_rate, sigma, Z, T):
    """
    Generates the terminal share price given some random normal values, z
    """
    # It returns an array of terminal stock prices.
    return S_0*np.exp((risk_free_rate-sigma**2/2)*T+sigma*np.sqrt(T)*Z)

# Creating 10000 simulations for future portfolio values
Z = np.matmul(L, norm.rvs(size= [3, t_simulations]))
portval_future = np.sum(terminal_shareprice(S_0, r, sigma, Z, T), axis=0)

# Calculating portfolio returns
port_return = (portval_future - portval_current)/portval_current

# Sorting the Returns
port_return = np.sort(port_return)

# Determining VaR
mVar_estimate = -port_return[int (np.floor(alpha*t_simulations))-1]

# Historical simulation
np.random.seed(0)
s0 = 25
sigma = 0.1
r = 0.1
T = 1
alpha = 0.05
t_simulations = 10000
dT = 1/365

def share_path(S_0, risk_free_rate, sigma, Z, dT):
    """
    Generates the terminal share price given some random normal values, Z
    """
    return S_0*np.exp(np.cumsum((risk_free_rate - sigma**2/2)*dT + sigma*np.sqrt(dT)*Z,1))

# generate synthetic share data

Z_histdata = norm.rvs(size = [3,5*365])
corr_Z = np.transpose(np.matmul(L, Z_histdata))
price_path = share_path(s0, r, sigma, corr_Z, dT)

# current portfolio value as the sum of the most recent share price
hist_s0 = price_path[-1]
hist_portval = np.sum(hist_s0)

# initialize a vector to capture simulated portfolio returns
hist_portret = [None]*t_simulations

# determining historical log returns
hist_lret = np.log(price_path[1:]) - np.log(price_path[0: -1])

# using historical returns to project future returns
for i in range(t_simulations):
    rand_samp = uniform.rvs(size=365)*(len(price_path)-1)
    rand_samp = [int(x) for x in rand_samp]
    
    share_returns = hist_lret[rand_samp]
    s_term = hist_s0*np.exp(np.sum(share_returns, axis=0))
    hist_portret[i] = (np.sum(s_term) - hist_portval)/hist_portval
    
# Sorting portfolio returns
hist_portret = np.sort(hist_portret)

# Historical VaR estimate
hVaR_estimate = -hist_portret[int(np.floor(alpha*t_simulations))-1]

plt.figure(figsize=(15,8))
plt.title("Distribution of Historical Portfolio Returns")
plt.xlabel("Portfolio Returns")
plt.ylabel("Times Calculated")
plt.hist(hist_portret, bins=30, ec="black")
plt.show()