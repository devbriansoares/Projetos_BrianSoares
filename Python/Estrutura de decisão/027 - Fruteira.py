print ("| FRUTEIRA |")

morangosComprados = float(input("Qtd de Morangos Comprados (Kg): "))
macasCompradas = float(input("Qtd de Maçãs Compradas (Kg): "))
valorMorango = 0
valorMaca = 0

if morangosComprados > 5:
    valorMorango = morangosComprados * 2.20
else:
    valorMorango = morangosComprados * 2.50

if macasCompradas > 5:
    valorMaca = macasCompradas * 1.50
else:
    valorMaca = macasCompradas * 1.80

qtdTotal = morangosComprados + macasCompradas
valorTotal = valorMaca + valorMorango
if valorTotal > 25 or qtdTotal > 8:
    valorTotal = valorTotal - (valorTotal*0.10)
    print ('''\nMorango: {}Kg
Maçã: {}Kg
Valor Total: R${:.2f}
    '''.format(morangosComprados,macasCompradas,valorTotal))
else:
    print ('''\nMorango: {}Kg
Maçã: {}Kg
Valor Total: R${:.2f}
    '''.format(morangosComprados,macasCompradas,valorTotal))