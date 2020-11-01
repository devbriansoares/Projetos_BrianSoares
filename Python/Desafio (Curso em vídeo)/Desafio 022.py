nome = input("Insira seu nome completo: ")
listaNome = nome.split()

print ()
print (nome.upper())
print (nome.lower())
print ("Quantas letras tem o nome completo (sem espaços)? {} letras".format(len(nome)-nome.count(" ")))
print ("Quantas letras tem o primeiro nome? {} letras".format (len(listaNome[0])))