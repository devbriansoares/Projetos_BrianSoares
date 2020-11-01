print ("| CÁLCULO DE PESO IDEAL HOMEM/MULHER |")
print ()

altura = float(input("Informe a altura em metros: "))
pesoH = ((72.7*altura) - 58)
pesoM = (62.1*altura) - 44.7

print ()
print ("O peso ideal para um homem desta altura é de: ","%.2f" % pesoH,"kg")
print ("O peso ideal para uma mulher desta altura é de: ","%.2f" % pesoM,"kg")

input()
