import random
print ("| SORTEIO PARA ORDEM DE APRESENTAÇÃO |")

listaNomes = []
for i in range(0,4):
    nome = input("\nNome do aluno: ")
    listaNomes.append(nome)
random.shuffle(listaNomes)
print ("\nOrdem de apresentação: {}.".format(listaNomes))