print ("| PRIMEIRO E ÚLTIMO NOME |")

nome = input("Insira seu nome completo: ").title().split()
print ("Olá, Sr.(a) {} {}!".format(nome[0],nome[-1]))