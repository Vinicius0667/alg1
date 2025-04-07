a, b, c = map(float, input().split())

if a != 0:
    delta = b ** 2 - 4 * a * c

    if delta >= 0:
        raiz_1 = (-b + delta ** (1 / 2)) / (2 * a)
        raiz_2 = (-b - delta ** (1 / 2)) / (2 * a)
        
        print(f'R1 = {raiz_1:.5f}')
        print(f'R2 = {raiz_2:.5f}')
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')