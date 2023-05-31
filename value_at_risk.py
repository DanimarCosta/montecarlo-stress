# We will import the necessary libraries

import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate
import scipy

# Plotting
import matplotlib.pyplot as plt
import seaborn
import matplotlib.mlab as mlab

#Statistical calculation
from scipy.stats import norm

# For warnings suppression
import warnings
warnings.filterwarnings("ignore")

# We will import the daily data of Amazon from yahoo finance
# Calculate daily returns
df = yf.download("ENAT3.SA", "2019-01-01", "2023-01-20")
df = df[['Close']]
df['returns'] = df.Close.pct_change()


# Now we will determine the mean and standard deviation of the daily returns 
# Plot the normal curve against the daily returns

mean = np.mean(df['returns'])
std_dev = np.std(df['returns'])

df['returns'].hist(bins=40, density=True, histtype='stepfilled', alpha=0.1)
df = df[['Close']]
df['returns'] = df.Close.pct_change()
df = df.dropna()
plt.hist(df.returns, bins=40)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()