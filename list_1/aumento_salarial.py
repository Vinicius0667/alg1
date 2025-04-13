# -*- coding: utf-8 -*-

salario = float(input())

if salario <= 400:
    reajuste = salario * 15 / 100
    print(f'Novo salario: {salario + reajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 15 %')
elif salario > 400 and salario <= 800:
    reajuste = salario * 12 / 100
    print(f'Novo salario: {salario + reajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 12 %')
elif salario > 800 and salario <= 1200:
    reajuste = salario * 10 / 100
    print(f'Novo salario: {salario + reajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 10 %')
elif salario > 1200 and salario <= 2000:
    reajuste = salario * 7 / 100
    print(f'Novo salario: {salario + reajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 7 %')
else:
    reajuste = salario * 4 / 100
    print(f'Novo salario: {salario + reajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 4 %')