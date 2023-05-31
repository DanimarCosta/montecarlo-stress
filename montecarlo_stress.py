import datetime
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Set start and end dates for retrieving stock price data
start_date = datetime.datetime(2023, 1, 17)
end_date = datetime.datetime(2023, 5, 20)

# Retrieve stock price data for the specified ticker symbol
ticker_symbol = 'ITUB4.SA'
stock = yf.download(ticker_symbol, start=start_date, end=end_date)
precos = stock["Close"]

returns = precos.pct_change()
ultimo_preco = precos[-1]

# Number of simulations and days
num_simulations = 1000
num_days = 22

simulacao_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    preco_series = []

    preco = ultimo_preco * (1 + np.random.normal(0, daily_vol))
    preco_series.append(preco)

    for y in range(num_days):
        preco = preco_series[count] * (1 + np.random.normal(0, daily_vol))
        preco_series.append(preco)

        count += 1

        if count == num_days - 1:
            break

    simulacao_df[x] = preco_series

# Plot the simulated price data
simulacao_df.plot(figsize=(10, 6))
plt.xlabel('Days')
plt.ylabel('Simulated Price')
plt.title('Monte Carlo Simulation')
plt.show()