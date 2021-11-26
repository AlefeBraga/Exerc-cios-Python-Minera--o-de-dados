#7.2 Crie um Python Script que realize o mesmo procedimento da questão anterior. No
#entanto, ao invés do conteúdo da lista nomes ser atribuído no próprio script, faça
#uma estrutura de repetição na qual ela leia uma string do usuário e adicione os nomes
#digitados por ele, um de cada vez, na lista nomes. O término da adição de nomes
#deve ser indicado quando o usuário inserir uma string vazia (”).

cont = dict()
nomes = list()
resp = ' '

while resp != ' ':
    resp = input('Insira um nome(digite "espaço" para para de inserir):\n')
    nomes += [resp.capitalize()]
nomes.remove('')

#nomes = ['Alefe', 'Marcelo', 'Alefe', 'Duda', 'Marcelo', 'Tarcisio', 'Alefe']

for nome in nomes:
    
    if nome in cont:
        cont[nome] += 1

    else:
        cont[nome] = 1

print(cont)