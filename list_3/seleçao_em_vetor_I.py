# -*- coding: utf-8 -*-

vetor = []
vetor_menor_que_dez = []

for i in range(100):
    vetor.append(float(input()))
    
    if vetor[i] <= 10:
        vetor_menor_que_dez.append(i)
        vetor_menor_que_dez.append(vetor[i])

for i in range(0, len(vetor_menor_que_dez), 2):
    print(f'A[{vetor_menor_que_dez[i]}] = {vetor_menor_que_dez[i + 1]}')