# -*- coding: utf-8 -*-
'''
Mesma coisa do `numeros_pares.py`
Só que para números impares
'''

value = int(input())

i = 1

while i <= value:
    if i % 2 == 1:
        print(i)
    i += 1