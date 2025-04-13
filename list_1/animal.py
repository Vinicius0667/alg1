vertebra = input()
tipo = input()
familia = input()

if vertebra == 'vertebrado':
    if tipo == 'ave':
        if familia == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif familia == 'onivoro':
        print('homem')
    else:
        print('vaca')
else:
    if tipo == 'inseto':
        if familia == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    elif familia == 'hematofago':
        print('sanguessuga')
    else:
        print('minhoca')