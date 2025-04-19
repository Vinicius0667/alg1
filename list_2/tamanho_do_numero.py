# -*- coding: utf-8 -*-
'''
Este é um problema do AVA
'''

number = int(input())

# Faz um contador de comprimento
count_len = 0

# Utilizaremos o 0 para escapar do loop, pois número não pode ser zero
# A condição `if` de dentro do loop não deixaria
while number != 0:
    # Divide o número por 10
    number /= 10
    # Incrementa contador de tamanho
    count_len += 1
    # Se o número for menor que 1 quer dizer que chegamos ao seu tamanho    
    if number < 1:
        # Fazemos uma condição de escape do loop for
        number = 0
        # Seria melhor usar o `break` para escape de loop, porém ignoraremos por hora
        
print(count_len)