#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a altura em metros: "))
pesoH = ((72.7*altura) - 58)
pesoM = ((62.1*altura) - 44.7)

print ("Peso ideal p/ um homem desta altura é de: {:.2f}kg".format(pesoH))
print ("Peso ideal p/ uma mulher desta altura é de: {:.2f}kg".format(pesoM))