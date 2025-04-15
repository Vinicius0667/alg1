# -*- coding: utf-8 -*-

# Começa de 2, pois ele é o par que começa da sequencia de
# 1 a 100
par = 2

# Enquanto par for menor que 100, o programa
# Executará as instruções abaixo
while par <= 100:
    # Verifica se a divisão por dois do número resulta em 0
    if par % 2 == 0:
        # Se sim ele imprime o número
        print(par)
    # Caso não imprima ou caso ele imprima ele irá
    # Somar 1 a variável
    par += 1
    