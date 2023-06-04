import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay

plt.style.use('ggplot')

# Definir datas de início e término para recuperar dados de preços de ações
start_date = datetime(2023, 1, 17)
end_date = datetime(2023, 5, 20)

# Dados de preços de ações para o símbolo especificado
ticker_symbol = 'ITUB4.SA'
stock = yf.download(ticker_symbol, start=start_date, end=end_date)
precos = stock["Close"]

returns = precos.pct_change()
ultimo_preco = precos[-1]

# Calcula os dias úteis
def obter_datas_uteis(data_inicio, num_dias):
    datas_uteis = pd.date_range(start=data_inicio, periods=num_dias, freq='B')
    return datas_uteis

# Numero de simulações e de dias
data_inicio = datetime(2023, 5, 20).date()  # Data personalizada de início
dias_uteis = 22
datas_uteis = obter_datas_uteis(data_inicio, dias_uteis)

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

# Atribuir as datas úteis ao dataframe simulacao_df
simulacao_df['Data'] = datas_uteis

# Definir a coluna de datas úteis como índice
simulacao_df.set_index('Data', inplace=True)

# Gráfico dos dados de preços simulados
fig, ax = plt.subplots(figsize=(10, 6))
for col in simulacao_df.columns:
    ax.plot(simulacao_df.index, simulacao_df[col], color='steelblue', alpha=0.1)

ax.set(xlabel='Dias úteis', ylabel='Preço Projetado', title='Projeção de Monte Carlo')
plt.show()

# Cálculo do VaR com confiança de 99% usando o método de Monte Carlo
retorno_acumulado = simulacao_df.pct_change().cumsum()
ultimo_retorno_acumulado = retorno_acumulado.iloc[-1]
sorted_retornos_simulados = ultimo_retorno_acumulado.sort_values()
confianca = 0.99
var_montecarlo = sorted_retornos_simulados.quantile(1 - confianca)
var_montecarlo_percent = var_montecarlo * 100 
print("VaR Monte Carlo (99%):", var_montecarlo_percent, "%")      

# Exportar dados para o Excel
simulacao_df.to_excel('dados_simulados.xlsx')