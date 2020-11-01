import random
print ("| SORTEIO PARA LIMPAR O QUADRO |")

listaNomes = []
for i in range(0,4):
    nome = input ("\nNome do Aluno: ").capitalize()
    listaNomes.append(nome)

escolhido = random.choice(listaNomes)
print ("\nE o felizardo foi: {}!!!!".format(escolhido))