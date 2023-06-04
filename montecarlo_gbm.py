import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
n_simulacoes = 10  # Número de simulações
n_dias = 252  # Número de dias de negociação em um ano
valor_inicial = 30.0  # Valor inicial da ação ITUB3
taxa_retorno = 0.05  # Taxa de retorno esperada (5% ao ano)
volatilidade = 0.2  # Volatilidade esperada (20% ao ano)

# Simulação de Monte Carlo
simulacoes = np.zeros((n_simulacoes, n_dias))
simulacoes[:, 0] = valor_inicial

for i in range(n_simulacoes):
    for j in range(1, n_dias):
        retorno = np.random.normal(taxa_retorno / n_dias, volatilidade / np.sqrt(n_dias))
        simulacoes[i, j] = simulacoes[i, j - 1] * (1 + retorno)

# Plot dos resultados
plt.figure(figsize=(12, 6))
plt.plot(simulacoes.T)
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.title('Simulação de Monte Carlo - ITUB3')
plt.grid(True)
plt.show()
