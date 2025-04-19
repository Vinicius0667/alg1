# -*- coding: utf-8 -*-
'''
Outro problema do AVA
'''

numero = int(input())

count = 0
numero_inteiro = 0

while numero >= 1:
    if numero % 2 == 1:
        numero_inteiro += 2 ** count
    count += 1
    numero //= 10
        
print(numero_inteiro)