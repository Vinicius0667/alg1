# -*- coding: utf-8 -*-

numero = int(input())

# Faz começar `i`` com o valor `1`
for i in range(1, 11):
    # Calcula a tabuada
    resultado = numero * i
    print (f'{i} x {numero} = {resultado}')