print ("| ORDEM DECRESCENTE |")
print ()

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
print ()

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print ("Ordem decrescente: %d > %d > %d" % (n1, n2, n3))
    else:
        print ("Ordem decrescente: %d > %d > %d" % (n1, n3, n2))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print ("Ordem decrescente: %d > %d > %d" % (n2, n1, n3))
    else:
        print ("Ordem decrescente: %d > %d > %d" % (n2, n3, n1))
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print ("Ordem decrescente: %d > %d > %d" % (n3, n1, n2))
    else:
        print ("Ordem decrescente: %d > %d > %d" % (n3, n2, n1))
else:
    print ("Erro na entrada de dados!")
    

input()
