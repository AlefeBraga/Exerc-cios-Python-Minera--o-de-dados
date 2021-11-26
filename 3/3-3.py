# 3.3 Ainda considerando as variáveis da questão anterior, o que poderia se fazer para que
# a + b tenha o mesmo resultado de c + d ou vice versa?

print("Resposta: Convertendo as variáveis em str e int");

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

SomaAB = str(a) + str(b);
SomaCD = int(c) + int(d);

print('A + B (str) = ', SomaAB);
print('C + D (int) = ', SomaCD);

# Retornou:
# A + B (str) =  12      -> Concatenou dois str
# C + D (int) =  3       -> Somou dois int