# 6.4 Faça um programa que liste para o usuário um menu com quatro opções, sendo cada
#   uma referente à uma operação matemática básica. Após o usuário ter escolhido a
#   opção, leia dois valores e realiza a operação selecionada.

print('Escolha a operacao:\n1)soma;\n2)subtracao;\n3)multiplicacao;\n4)divisao.')

resp = int(input('Resposta: '))

a = float(input('a = '))
b = float(input('\nb = '))

if resp == 1:
    print('a + b =', a+b)
elif resp == 2:
    print('a − b =', a-b)
elif resp == 3:
    print('a ∗ b =', a*b)
elif resp == 4:
    print('a / b =', a/b)
else:
    print('Operacao invalida ')
