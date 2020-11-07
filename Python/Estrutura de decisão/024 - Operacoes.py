print ("| OPERAÇÕES |")

num1 = float(input("\nNúmero 1: "))
num2 = float(input("Número 2: "))
result = 0

operacao = input('''
Digite '+' para Soma
Digite '-' para Subtração
Digite '*' para Multiplicação
Digite '/' para Divisão

Operação: ''')

if operacao == "+":
    result = num1 + num2
    print ("\nResultado: {:.2f}".format(result))
elif operacao == "-":
    result = num1 - num2
    print ("\nResultado: {:.2f}".format(result))
elif operacao == "*":
    result = num1 * num2
    print ("\nResultado: {:.2f}".format(result))
elif operacao == "/":
    result = num1 / num2
    print ("\nResultado: {:.2f}".format(result))

print ("Par" if result % 2 == 0 else "Ímpar")
print ("Positivo" if result >= 0 else "Negativo")
print ("Inteiro" if (round(result)-result) == 0 else "Decimal")