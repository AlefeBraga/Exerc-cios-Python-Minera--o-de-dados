# 4.2 Repita o processo da questão anterior, porém utilizando a função deg2rad 
# da biblioteca numpy para converter o ângulo de graus para radianos.

from numpy import deg2rad

from math import pi, sin, cos ,tan 

#valor = float(input('Insira o valor do angulo'))
valor = 100
valorRad = deg2rad(valor)

print('seno = ', sin(valorRad))
print('Cosseno = ',cos(valorRad))
print('tangente = ',tan(valorRad))