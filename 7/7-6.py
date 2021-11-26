N = int(input('Número N:\n'))

L = list()

for i in range(N):
    x = float(input('Digite um número para a lista:\n'))
    L.append(x)

print(L)

soma = 0
min = L[0]
max = L[0]

for i in L:
    soma += i
    if min > i:
        min = i
    if max < i:
        max = i

print('Soma = ', soma)
print('Média = ', soma/N)
print('Maior = ', max)
print('Menor = ', min)