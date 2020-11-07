print ("| POSTO DE COMBUSTÍVEIS |")

litros = float(input("Litros vendidos: "))
combustivel = input("G - Gasolina / A - Álcool: ").upper()
precoGasolina = 2.50
precoAlcool = 1.90
valorTotal = 0

if combustivel == "A":
    valorTotal = (precoAlcool * litros)
    if litros <= 20:
        valorTotal = valorTotal - (valorTotal*0.03)
        print ("\n{}L + 3% De desconto por R${:.2f}.".format(litros,valorTotal))
    else:
        valorTotal = valorTotal - (valorTotal*0.05)
        print ("\n{}L + 5% De desconto por R${:.2f}.".format(litros,valorTotal))
elif combustivel == "G":
    valorTotal = (precoGasolina * litros)
    if litros <= 20:
        valorTotal = valorTotal - (valorTotal*0.04)
        print ("\n{}L + 4% De desconto por R${:.2f}.".format(litros,valorTotal))
    else:
        valorTotal = valorTotal - (valorTotal*0.06)
        print ("\n{}L + 6% De desconto por R${:.2f}.".format(litros,valorTotal))