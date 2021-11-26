# 5.2 Faça um Python Script que receba um valor t referente a uma quantidade total em
#  segundos. Calcule a quantas horas:minutos:segundos a quantidade total de segudos
#  corresponde.

t = 90 #int(input('Digite o tempo total em segundos:\n'))

segundos = t%60

t //= 60

min = t%60

t //= 60

horas = t

print('O tempo digitado equivale a:\n',horas , ':',min , ':', segundos , sep='')
