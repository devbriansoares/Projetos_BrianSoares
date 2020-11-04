print ("| CALCULADORA BÁSICA |")

def soma (num1,num2):
    return num1+num2
def sub (num1,num2):
    return num1-num2
def mult (num1,num2):
    return num1*num2
def div (num1,num2):
    return num1/num2
    
print ('''
Digite '+' para Soma
Digite '-' para Subtração
Digite '*' para Multiplicação
Digite '/' para Divisão
''')

while True:
    inputError = False
    try:
        operacao = input("Qual operação você deseja realizar? ")
    except ValueError:
        inputError = True

    if inputError == True:
        print ("Digite um símbolo válido presente no Menu!")
    elif operacao not in ["+","-","*","/"]:
        print ("Digite um símbolo válido presente no Menu!")
    else:
        try:
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))
        except ValueError:
            inputError = True
        if inputError == True:
            print ("_________________________")
            print ("Valor de entrada inválido!")
        else:
            if operacao == "+":
                print ("{} + {}= {}".format(num1,num2,soma(num1,num2)))
                break
            elif operacao == "-":
                print ("{} - {}= {}".format(num1,num2,sub(num1,num2)))
                break
            elif operacao == "*":
                print ("{} * {}= {}".format(num1,num2,mult(num1,num2)))
                break
            elif operacao == "/":
                print ("{} / {}= {}".format(num1,num2,div(num1,num2)))
                break
            else:
                print ("----------ERRO NA OPERAÇÃO----------")


