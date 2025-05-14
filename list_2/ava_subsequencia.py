# -*- coding: utf-8 -*-

quantidade_de_numeros = int(input())

sequencia_maior = 0
sequencia_atual = 1
numero = int(input())
numero_anterior = numero

for _ in range(quantidade_de_numeros - 1):
    numero = int(input())
    
    if numero_anterior >= numero:
        if sequencia_maior < sequencia_atual:
            sequencia_maior = sequencia_atual
        sequencia_atual = 0
    numero_anterior = numero
    sequencia_atual += 1

if sequencia_maior == 0 or sequencia_atual > sequencia_maior:
    sequencia_maior = sequencia_atual

print(sequencia_maior)