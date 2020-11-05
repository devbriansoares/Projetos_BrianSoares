print ("| RADAR ELETRÔNICO |")

velocidade = float(input("Insira a velocidade: "))
if velocidade > 80:
    print ("\nVOCÊ FOI MULTADO!")
    print ("Valor da multa: R${:.2f}".format((velocidade-80)*7))
else:
    print ("\nVocê está dentro do limite de velocidade!")