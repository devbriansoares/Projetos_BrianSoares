print ("| CONTADOR DE STRING |")

frase = input("Digite uma frase: ").upper().strip()
print ("\nA primeira posição em que aparece a letra A é: {}ª posição".format(frase.find('A')+1))
print ("A última posição em que aparece a letra A é: {}ª posição".format(frase.rfind('A')))
print ("Quantidade de vezes que aparece a letra A: {}".format(frase.count("A")))