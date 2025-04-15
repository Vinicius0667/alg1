# -*- coding: utf-8 -*-

value = int(input())
count = 0

# Irá executar o código 6 vezes
while count < 6:
    # Verifica se o valor é impar
    if value % 2 == 1:
        print(value)
        # Incrementa dois para o próximo impar
        value += 2
    # Verifica se é par
    elif value % 2 == 0:
        # Se for par incremente 1
        value += 1
        print(value)
        value += 2
    count += 1