# -*- coding: utf-8 -*-

'''
Favor olhar o arquivo `numeros_positivos.py`
Para ter uma explicação de cada linha,
Neste código só explicarei a média
'''

i = 0
count = 0
media = 0

while i < 6:
    numero = float(input())
    if numero > 0:
        # Incrementa o valor dos números positivos
        media += numero
        count += 1
    i += 1
# Faz o calculo da média
# E armazena o resultado na própria variável `media` 
media /= count

print(f'{count} valores positivos')
print(f'{media:.1f}')