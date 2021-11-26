# 6.1 Faça um código que receba um número n do usuário e imprima os n primeiros
#     números da sequência de Fibonacci.

n = int(input('Ate qual numero da sequencia de fibonacci deseja ver?\n'))

f = 0

aux1 = 1

aux2 = 0

print('Indice 1 f = 1')

for i in range(2, n+1):
    f = aux1 + aux2
    aux2 = aux1
    aux1 = f
    print('Indice', i, 'f =', f)