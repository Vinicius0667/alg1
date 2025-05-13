# -*- coding: utf-8 -*-

x = float(input())
k = int(input())

fatorial = 1
resultado = 1
aux = -1

for i in range(2, k + 1, 2):
    for n in range(i, 1, -1):
        fatorial *= n
    resultado += aux * (x ** i / fatorial)
    fatorial = 1
    aux *= -1
    
print (f'{resultado:.4f}')