# -*- coding: utf-8 -*-

numeros_a_ler = int(input())

for i in range(numeros_a_ler):
    numero = int(input())
    if numero != 0:
        if numero % 2 == 0:
            print('EVEN', end=' ')
        else:
            print('ODD', end=' ')
        if numero > 0:
            print('POSITIVE')
        elif numero < 0:
            print('NEGATIVE')
    else:
        print('NULL')