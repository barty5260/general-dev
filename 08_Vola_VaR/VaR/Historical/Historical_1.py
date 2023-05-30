import pandas as pd
import numpy as np
import re
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
quandl.ApiConfig.api_key = "<your API key>" #get on Quandl.com
portfolio = quandl.get(["WIKI/AAPL", "WIKI/GE", "WIKI/GOOGL", "WIKI/JNJ"],\
start_date="2015-03-12", end_date="2016-03-12",\
transformation="rdiff") 
portfolio.head()

returns = portfolio[list(portfolio.columns[portfolio.columns.str.\
                    contains('Adj. Close')])]
returns = returns.rename(columns={"WIKI/AAPL — Adj. Close":"AAPL",\
                                  "WIKI/GE — Adj. Close":"GE",\
                                 "WIKI/GOOGL — Adj. Close":"GOOGL",\
                                 "WIKI/JNJ — Adj. Close":"JNJ"})
returns = returns * 100 #convert to percentages
returns.head()

#Convert returns into P/L
weights = [0.2, 0.3, 0.1, 0.4] 
PnL = (weights * returns.values).sum(axis=1)

historic_var = np.percentile(PnL, 5, interpolation="lower")
print(f'The simple historical VaR is {historic_var}')


from scipy.stats import kurtosis, skew
print(f"Skew is {skew(PnL)}\n")
print(f"Kurtosis is {kurtosis(PnL)}")