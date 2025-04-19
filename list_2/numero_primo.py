# -*- coding: utf-8 -*-

'''
Mais um exercício do AVA
'''

numero = int(input())

divisor = 2
primo = True

while divisor ** 2 <= numero and primo:
    if numero % divisor == 0:
        primo = False
    divisor += 1
    
if primo:
    print('Primo')
else:
    print('Composto')