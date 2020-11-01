print ("| PRODUTO MAIS BARATO |")
print ()

prod1 = float(input("Produto 1: "))
prod2 = float(input("Produto 2: "))
prod3 = float(input("Produto 3: "))
print ()

if prod1 < prod2 and prod1 < prod3:
    print ("O Produto 1 é o mais barato!")
elif prod2 < prod1 and prod2 < prod3:
    print ("O Produto 2 é o mais barato!")
elif prod3 < prod1 and prod3 < prod2:
    print ("O Produto 3 é o mais barato!")
else:
    print ("Erro na entrada de dados!")


input()
