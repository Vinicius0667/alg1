seg = int(input())

minutos = int(seg / 60)
seg -= minutos * 60
hora = int(minutos / 60)
minutos -= hora * 60 

print(f'{hora}:{minutos}:{seg}')