print ("| MAIOR DOS TRÊS |")
print("\nDIGITE 3 NÚMEROS PARA SABER QUAL É O MAIOR")

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

if n1 > n2 and n1 > n3:
    print ("Número 1 é o maior!")
elif n2 > n1 and n2 > n3:
    print ("Número 2 é o maior!")
elif n3 > n1 and n3 > n2:
    print ("Número 3 é o maior!")
else:
    print ("Os três números são iguais!")