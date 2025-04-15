# -*- coding: utf-8 -*-
'''
Favor olhar o arquivo `numeros_positivos.py`
Para ter uma explicação de cada linha,
O código é o mesmo, só muda as outras operações
'''

i = 0
count_pares = 0
count_impares = 0
count_positivos = 0
count_negativos = 0

while i < 5:
    numero = float(input())
    # Verifica se é par
    if numero % 2 == 0:
        count_pares += 1
    # Verifica se é impar
    elif numero % 2 == 1:
        count_impares += 1
    # Verifica se é positivo
    if numero > 0:
        count_positivos += 1
    # Verifica se é negativo
    elif numero < 0:
        count_negativos += 1
    i += 1

print(f'{count_pares} valor(es) par(es)')
print(f'{count_impares} valor(es) impar(es)')
print(f'{count_positivos} valor(es) positivo(s)')
print(f'{count_negativos} valor(es) negativo(s)')