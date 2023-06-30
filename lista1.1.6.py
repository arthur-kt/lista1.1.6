"""
Lista 1, parte 1, exercício 6

Descrição: Este programa apresenta a resolução de uma questão da lista 1 da cadeira de Economia Computacional
Autor:Arthur Kafrouni Tomazi
Data: 23/06/2023
Versão: 0.0.1
"""

# Atribuição de variaveis

n = 0
pa_0 = 0
pa_n = 0
r = 0
soma_pa = 0

# Entrada de dados

n = float(input("Quantidade de termos (n): "))
pa_0 = float(input("Primeiro termo: "))
r = float(input("Razão: "))

# Processamento de dados

pa_n = pa_0 + (n-1)*r
soma_pa = (n*(pa_0 + pa_n))/2

# Saída de dados

print(f'A progressão aritimética que contém {n} termos, começando pelo termo {pa_0} e de razão {r}, resulta no termo final {pa_n} e a soma de seus termos é {soma_pa}')