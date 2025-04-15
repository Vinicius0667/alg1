# -*- coding: utf-8 -*-

# Inicializa o contador de repetições
i = 0
# Inicializa o contador de positivos
count = 0

# Fará o código abaixo até que i seja igual ou menor a 6
while i < 6:
    # Recebe o número digitado
    numero = float(input())
    # Compara se o número é positivo
    if numero > 0:
        # Incrementa no contador de positivos
        count += 1
    # Incrementa no contador de loop
    i += 1
# Imprime o resultado
print(f'{count} valores positivos')