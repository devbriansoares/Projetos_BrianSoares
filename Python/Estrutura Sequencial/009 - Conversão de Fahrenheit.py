#Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.
F = float(input("Temperatura em Fahrenheit: "))
C = 5*((F-32)/9)

print ("\nTemperatura em Graus Celsius: {:.2f}°".format(C))