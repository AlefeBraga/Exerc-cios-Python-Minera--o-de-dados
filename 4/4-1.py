# 4.1 Peça do usuário um valor em graus para um ângulo. Converta-o para radianos e,
# usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.

from math import pi, sin, cos ,tan 

#valor = float(input('Insira o valor do angulo'))
valor = 30
valorRad = valor * (pi/180)

print('seno = ', sin(valorRad))
print('Cosseno = ',cos(valorRad))
print('tangente = ',tan(valorRad))