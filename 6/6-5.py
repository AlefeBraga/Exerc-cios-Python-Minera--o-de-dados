# 6.5 Faça um programa que receba um número inteiro n e o fatore.

num = int(input('Digite um numero para fatorar\n'))

i = 2

while i <= num:
    if num%i == 0:
        print(i, end = ' ')
        num //= i
    else:
        i += 1