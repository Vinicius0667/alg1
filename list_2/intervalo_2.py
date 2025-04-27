# -*- coding: utf-8 -*-

# Recebemos a quantidade de números a ler
numeros_a_ler = int(input())
in_range = 0
out_range = 0

# Executaremos o bloco de instruções para cada valor de `numeros_a_ler`
for i in range(numeros_a_ler):
    numero = int(input())
    
    # Verificamos se ele está no intervalo
    if numero >= 10 and numero <= 20:
        in_range += 1
    else:
        out_range += 1

print(in_range, 'in')
print(out_range, 'out')