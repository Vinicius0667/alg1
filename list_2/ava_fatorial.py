# -*- coding: utf-8 -*-

'''
Exercício do AVA
'''

numero = int(input())

# Verifica se o número é zero
if numero != 0:
    fatorial = numero
    # Faz a variável `i` começar de `(numero - 1)` de zero e ir até 2 de -1 em -1
    for i in range(numero - 1, 1, -1):
        # Faz o calculo do fatorial
        fatorial *= i
    # Imprimi resultado
    print(fatorial)
else:
    print('1')