# -*- coding: utf-8 -*-

def fibonacci (number):
    before_number = 0
    fib = 1
    print('0 1', end=' ')
    for i in range(number - 2):
        aux = fib
        fib += before_number
        if i == number - 3:
            print(fib)
        else:
            print(fib, end=' ')
        before_number = aux

n = int(input())

if n < 46 and n > 0:
    fibonacci(n)
