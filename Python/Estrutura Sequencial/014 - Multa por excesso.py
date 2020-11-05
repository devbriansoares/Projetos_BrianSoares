multa = 4
peso = float(input("Informe o peso do peixe em Kg: "))
if peso > 50:
    excesso = (peso-50)
    multaTotal = (multa*excesso)
    print ("O valor total da multa é de: R${:.2f}".format(multaTotal))
else:
    print ("Peso menor ou igual ao estabelecido em regulamento!")