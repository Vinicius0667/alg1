# -*- coding: utf-8 -*-

decimal = int(input())
ternario = 0
count = 1

while decimal >= 1:
    resto = decimal % 3
    decimal //= 3
    
    ternario += resto * count
    count *= 10

print(ternario)    
