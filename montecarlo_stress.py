import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Parâmetros
n_simulacoes = 10000  # Número de simulações
n_dias = 75  # Número de dias de negociação no período

# Obter dados históricos
ticker = 'ITUB3.SA'
start_date = '2023-01-17'
end_date = '2023-05-20'

data = yf.download(ticker, start=start_date, end=end_date)
prices = data['Close']

# Definir valor inicial como o fechamento de 20/05/2023
valor_inicial = prices[-1]

# Cálculo da taxa de retorno esperada e volatilidade
returns = prices.pct_change().dropna()
taxa_retorno = np.mean(returns) * 252  # Taxa de retorno esperada (retorno médio anualizado)
volatilidade = np.std(returns) * np.sqrt(252)  # Volatilidade anualizada

# Simulação de Monte Carlo
simulacoes = np.zeros((n_simulacoes, n_dias))
simulacoes[:, 0] = valor_inicial

for i in range(n_simulacoes):
    for j in range(1, n_dias):
        retorno = np.random.normal(taxa_retorno / n_dias, volatilidade / np.sqrt(n_dias))
        simulacoes[i, j] = simulacoes[i, j - 1] * (1 + retorno)

# Cálculo do VaR
nivel_confianca = 0.95  # Nível de confiança
simulacoes_finais = simulacoes[:, -1]
simulacoes_finais_ordenadas = np.sort(simulacoes_finais)
var_posicao = int(n_simulacoes * (1 - nivel_confianca))
var = simulacoes_finais_ordenadas[var_posicao]

# Plot dos resultados
plt.figure(figsize=(12, 6))
plt.plot(simulacoes.T)
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.title(f'Simulação de Monte Carlo - ITUB3\nVaR ({nivel_confianca*100}%): {var:.2f}')
plt.grid(True)
plt.show()
