# 7.3 Crie um programa que lê uma mensagem do usuário. Com esta mensagem, faça uma
#  nova omitindo trocando todos os caracteres de nomes próprios por ’*’. Exemplo:
#  se a mensagem for ’Lucas foi ao shopping com Fernanda assistir aquele filme da
#  Marvel’, a nova mensagem deverá ser ’***** foi ao shopping com ******** assistir
#  aquele filme da ******’. Assuma que um nome próprio sempre começa com letra
#  maiúscula e contém apenas letras.

msg = input('Digite uma mensagem:\n')

NovaMSG = str()

for i in msg:
    if i.isupper ():
        flag = True
        NovaMSG += '∗'
        continue
    if flag :
            if i.isalpha ():
                NovaMSG += '∗'
                continue
            else:
                NovaMSG += i
                flag = False
    else:
        NovaMSG += i

print(NovaMSG)