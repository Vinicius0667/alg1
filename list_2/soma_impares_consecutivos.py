# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y + 1
    y = aux
# Instancia a variável soma com 0
soma = 0

# Faremos a soma de todos os impares de x até y
while x < y:
    # Caso x seja um número par
    if x % 2 == 0:
        # Adicionaremos +1 para transforma-lo em impar
        x += 1
        # Armazenamos em soma
        soma += x
    else:
        soma += x
    # Aumentamos o valor de x em 2 para o próximo impar
    x += 2

print(soma)