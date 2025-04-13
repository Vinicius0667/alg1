a, b, c = map(float, input().split())

if b < c:
    aux = c
    c = b
    b = aux

if a < c:
    aux = a
    a = c
    c = aux

if a < b:
    aux = a
    a = b
    b = aux

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
    if a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
    if a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c and a == c:
        print('TRIANGULO EQUILATERO')
    if a == b and a != c or a == c and a != b or b == c and b != a:
        print('TRIANGULO ISOSCELES')