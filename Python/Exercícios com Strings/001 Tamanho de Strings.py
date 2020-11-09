a = input("Digite: ")
b = input("Digite: ")

print ("\nTamanho de '{}': {} caracteres.".format(a,len(a)))
print ("Tamanho de '{}': {} caracteres.".format(b,len(b)))

if len(a) == len(b):
    print ("As duas strings são de tamnhos iguais!")
else:
    print ("As duas strings são de tamanhos diferentes!")

if a == b:
    print ("As duas strings possuem conteúdo igual!")
else:
    print ("As duas strings possuem conteúdo diferente!")