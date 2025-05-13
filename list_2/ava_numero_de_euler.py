# -*- coding: utf-8 -*-

x = float(input())
n = int(input())

fatorial = 1
resultado = 1

for i in range(1, n + 1, 1):
    for n in range(i, 1, -1):
        fatorial *= n
    resultado += (x ** i / fatorial)
    fatorial = 1
    
print (f'{resultado:.4f}')