# 7.1 Crie um Python Script que conte quantas vezes cada nome está presente em uma
#  lista [’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome1’:
#  xvezes, ’nome2’: yvezes, ....}.

cont = dict()

nomes = ['Alefe', 'Marcelo', 'Alefe', 'Duda', 'Marcelo', 'Tarcisio', 'Alefe']

for nome in nomes:
    
    if nome in cont:
        cont[nome] += 1

    else:
        cont[nome] = 1

print(cont)