# -*- coding: utf-8 -*-

n = int(input())
x = 1
pi = 0

for i in range(1, n + 1, 2):
    pi += x * 4 / i
    x *= -1
    
print(f'{pi:.4f}')