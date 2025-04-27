# -*- coding: utf-8 -*-

'''
Exercício do AVA
'''

n = int(input())
result = 1

# Faz um for, onde `i` inicial com 2 e vai até i == n
for i in range(2, n + 1):
    # Calcula a divisão
    result += 1 / i
print(f'{result:.4f}')