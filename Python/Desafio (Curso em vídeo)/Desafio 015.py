print ("| ALUGUEL DE CARROS |")
print ()

dia = 60
kmValor = 0.15

kmRodado = float(input("Quantos km o carro percorreu? "))

valorTotal = (dia+(kmValor*kmRodado))
print ("\nValor a ser pago: R${:.2f}".format(valorTotal))