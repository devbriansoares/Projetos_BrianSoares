print ("| COMPARATIVO DE NÚMEROS |")

num = [0,0]
x = 0
while x < 2:
    num[x] = float(input("Número {}: ".format(x+1)))
    x +=1
if num[0] > num[1]:
    print ("O primeiro valor é maior. {} > {}.".format(num[0],num[1]))
elif num[1] > num[0]:
    print ("O segundo valor é maior. {} > {}.".format(num[1],num[0]))
else:
    print ("Não existe valor maior. Os dois são iguais!")