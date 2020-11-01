w = float(input("Largura: "))
h = float(input("Altura: "))
a = (w*h)
l = 2

result = (a/l)

print ("Para uma parede de área {:.2f}m² você precisará de {:.2f}L de tinta.".format(a,result))