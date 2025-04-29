# -*- coding: utf-8 -*-

'''
Código do AVA
'''

numero = int(input())

count = 1

while count != numero + 1:
    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('Buzz')
    else:
        print(count)
    count += 1
    