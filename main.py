# -*- coding: utf-8 -*-
# *** Spyder Python IDLE***

import random
import matplotlib.pyplot as plt

def teste_stress(valor_inicial, taxa_retorno, num_simulacoes):
    resultados = []
    
    for _ in range(num_simulacoes):
        valor = valor_inicial
        for _ in range(12):  # número de meses
            retorno = random.uniform(-0.1, 0.1)  # retorno aleatório entre -10% e 10%
            valor *= (1 + taxa_retorno + retorno)
        resultados.append(valor)
    
    return resultados

# Parâmetros do teste de estresse
valor_inicial = 100000  # valor inicial do investimento
taxa_retorno = 0.05  # taxa de retorno esperada por mês
num_simulacoes = 10000  # número de simulações

# Executa o teste de estresse
simulacoes = teste_stress(valor_inicial, taxa_retorno, num_simulacoes)

# Plota o histograma dos resultados
plt.hist(simulacoes, bins=30, edgecolor='black')
plt.xlabel('Valor do Investimento')
plt.ylabel('Frequência')
plt.title('Distribuição dos Resultados do Teste de Estresse')
plt.show()