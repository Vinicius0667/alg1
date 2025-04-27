# -*- coding: utf-8 -*-

'''
Exercício do AVA
'''

n = int(input())
subnumero = 0
count = 1

# Repetiremos o loop até `n` for  menor que 1
while n >= 1:
    # Pegaremos o resto dessa conta
    resto = n % 10
    # Dividimos o número por 10 e retiramos o resto
    n //= 10
    # Se for par pegamos e armazenamos no `subnumero`
    if resto % 2 == 0:
        subnumero += resto * count
        count *= 10
# Imprimimos o resultado, se não tiver digito par, o zero será impresso por padrão
print(subnumero)