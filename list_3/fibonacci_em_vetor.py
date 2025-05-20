# -*- coding: utf-8 -*- 

def fibonacci ():
    vetor = [0, 1, 1]
    for i in range(2, 60):
        vetor.append(vetor[i] + vetor[i - 1])
    return vetor

def main():
    sequencia_fibonacci = fibonacci()
    t = int(input())
    for _ in range(t):
        posicao = int(input())
        print(f'Fib({posicao}) = {sequencia_fibonacci[posicao]}')
main()