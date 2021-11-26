
#valor = int(input('Digite o valor:\n'))

valor = 377

nota100 = valor//100
valor = valor%100

nota50 = valor//50
valor = valor%50

nota10 = valor//10
valor = valor%10

nota1 = valor//1
valor = valor%1

print('100 ,00 reais:', nota100)
print('50 ,00 reais:', nota50)
print('10 ,00 reais:', nota10)
print('N1,00 real:', nota1)
