sexo = input("Sexo (M/F): ").upper()
altura = float(input("Informe a altura em metros: "))
if sexo == "M":
    pesoM = ((72.7*altura) - 58)
    print ("Seu peso ideal é de: {:.2f}kg".format(pesoM))
elif sexo == "F":
    pesoF = ((62.1*altura) - 44.7)
    print ("Seu peso ideal é de: {:.2f}kg".format(pesoF))
