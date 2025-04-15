# -*- coding: utf-8 -*-
'''
Favor olhar o arquivo `numeros_positivos.py`
Para ter uma explicação de cada linha,
O código é o mesmo, só muda que são pare
'''

i = 0
count = 0

# Desta vez o loop ocorrerá 5 vezes somente
while i < 5:
    numero = float(input())
    # Verificamos se é par
    if numero % 2 == 0:
        count += 1
    i += 1
print(f'{count} valores pares')