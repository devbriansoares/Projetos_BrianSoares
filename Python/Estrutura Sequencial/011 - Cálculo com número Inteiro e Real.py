#Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre:
#A) O produto do dobro do primeiro com metade do segundo .
#B) A soma do triplo do primeiro com o terceiro.
#C) O terceiro elevado ao cubo.
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um número inteiro: "))
num3 = float(input("Informe um número real: "))

print ("\nResultado A: {:.2f}".format((num1*2)*(num2/2)))
print ("Resultado B: {:.2f}".format((num1*3)+(num3)))
print ("Resultado C: {:.2f}".format(num3**3))