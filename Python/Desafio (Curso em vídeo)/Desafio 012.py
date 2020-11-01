valor = float(input("Valor: "))
desc = 5
valorNovo = (valor-(valor*(desc/100)))

print ("Valor pago com {}% de desconto foi de R${:.2f}.".format (desc,valorNovo))