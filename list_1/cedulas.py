valor = int(input())

print(valor)

cem = int(valor / 100)
valor -= cem * 100
print(f'{cem} nota(s) de R$ 100,00')

cinquenta = int(valor / 50)
valor -= cinquenta * 50
print(f'{cinquenta} nota(s) de R$ 50,00')

vinte = int(valor / 20)
valor -= vinte * 20
print(f'{vinte} nota(s) de R$ 20,00')

dez = int(valor / 10)
valor -= dez * 10
print(f'{dez} nota(s) de R$ 10,00')

cinco = int(valor / 5)
valor -= cinco * 5
print(f'{cinco} nota(s) de R$ 5,00')

dois = int(valor / 2)
valor -= dois * 2
print(f'{dois} nota(s) de R$ 2,00')
print(f'{valor} nota(s) de R$ 1,00')