v1, v2, v3 = map(int, input().split())

l1 = v1
l2 = v2
l3 = v3

if v2 > v3:
    aux = v3
    v3 = v2
    v2 = aux

if v1 > v3:
    aux = v1
    v1 = v3
    v3 = aux

if v1 > v2:
    aux = v1
    v1 = v2
    v2 = aux

print(f'{v1}\n{v2}\n{v3}\n')
print(f'{l1}\n{l2}\n{l3}')