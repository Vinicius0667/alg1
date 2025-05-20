# -*- coding: utf-8 -*-

vetor = []

for _ in range(20):
    vetor.append(int(input()))

for i in range((int(len(vetor) / 2))):
    aux = vetor[i]
    vetor[i] = vetor[len(vetor) - (i + 1)]
    vetor[len(vetor) - (i + 1)] = aux

for i in range(20):
    print(f'N[{i}] = {vetor[i]}')