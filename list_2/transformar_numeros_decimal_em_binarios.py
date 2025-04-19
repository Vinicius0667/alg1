# -*- coding: utf-8 -*-

'''
Mais um código do AVA
'''

numero = int(input())

binario = 0
count = 0

while numero >= 1:
    resto = numero % 2
    binario = resto * 10 ** count + binario
    numero //= 2
    count += 1

print(binario)