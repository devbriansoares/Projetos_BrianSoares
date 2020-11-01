print ("| ANO BISSEXTO |")
print ()
print ()

ano = int(input("Ano: "))
print ()

if ano % 4 == 0 or ano % 400 == 0:
    print ("O valor informado é de um ano bissexto.")
elif ano % 100 == 0 or ano % 4 != 0:
    print ("O valor informado não é de um ano bissexto.")
else:
    print ("Valor inválido")

input ()
