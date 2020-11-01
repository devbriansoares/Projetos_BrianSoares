import random
print ("| SIMULADOR DE DADOS |")
print ()

while True:
    dado = 0
    jogarDado = input("Deseja lançar o dado s/n: ")
    jogarDado = jogarDado.lower()
    if jogarDado == "s":
        dado = random.randint(1,6)
        print (dado)
        print ()
    elif jogarDado == "n":
        print ("Programa encerrado")
        break
    else:
        print ("Valor informado inválido")
        print ()