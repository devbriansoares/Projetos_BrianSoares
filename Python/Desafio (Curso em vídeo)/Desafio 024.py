print ("| VERIFICAR PRIMEIRAS LETRAS DE UM TEXTO |")

palavra = input("Informe o nome de uma cidade: ").capitalize().split()
if palavra[0] == "Santo":
    print (True)
else:
    print (False)