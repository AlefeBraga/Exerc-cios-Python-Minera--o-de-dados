# 3.2 Considere as variáveis: a = 1; b = 2; c = ’1’; d = ’2’. 
# Utilizando o operador "+"observe a diferença entre somar a + b e somar c + d. 
# Qual a diferença e por que isso ocorre?

a = 1; 
b = 2; 
c = '1'; 
d = '2';

SomaAB = a + b;
SomaCD = c + d;

print('A + B = ', SomaAB);
print('C + D = ', SomaCD);

# Retornou:
# A + B =  3      -> Somou dois int
# C + D =  12     -> Concatenou dois str

