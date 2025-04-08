cod, quantidade = map(int, input().split())

if cod == 1:
    print(f'Total: R$ {4 * quantidade:.2f}')
elif cod == 2:
    print(f'Total: R$ {4.5 * quantidade:.2f}')
elif cod == 3:
    print(f'Total: R$ {5 * quantidade:.2f}')
elif cod == 4:
    print(f'Total: R$ {2 * quantidade:.2f}')
else:
    print(f'Total: R$ {1.5 * quantidade:.2f}')