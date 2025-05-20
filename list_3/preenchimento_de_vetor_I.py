# -*- coding: utf-8 -*- 

valor = int(input())
vetor = []
vetor.append(valor)
print(f'N[0] = {valor}')

for i in range(1, 10):
    vetor.append(vetor[i - 1] * 2)
    print(f'N[{i}] = {vetor[i]}')