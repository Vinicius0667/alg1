# -*- coding: utf-8 -*-

repeticoes = int(input())
numero_anterior = 1
fibonacci = 2

if repeticoes <= 0 or repeticoes <= 2:
    fibonacci = repeticoes
    if repeticoes == 2:
        fibonacci = 1

for i in range(2, repeticoes - 1):
    aux = fibonacci
    fibonacci += numero_anterior
    numero_anterior = aux 
print(fibonacci)