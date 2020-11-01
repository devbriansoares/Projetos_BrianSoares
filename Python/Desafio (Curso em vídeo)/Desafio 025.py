print ("| PROCURAR UMA STRING DENTRO DA OUTRA |")
print ("\nVerificar o sobrenome 'SILVA'.")
nome = input("\nInforme um nome completo: ").capitalize().split()
if "silva" in nome:
    print (True)
else:
    print (False)