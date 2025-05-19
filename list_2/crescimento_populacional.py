# -*- coding: utf-8 -*-

def crescimento(pa, pb, g1, g2):
    contador = 0
    while pa <= pb:
        pa = int(pa * g1)
        pb = int(pb * g2)
        contador += 1
        if contador > 100:
            break
    return contador

t = int(input())

for _ in range(t):
    numeros = input()
    numeros = list(numeros.split(' '))
    anos = crescimento(int(numeros[0]), int(numeros[1]), float(numeros[2]) / 100 + 1, float(numeros[3]) / 100 + 1)
    if (anos > 100):
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')