import random
print ("| SIMULADOR DE DADOS |")

while True:
    dado = 0
    jogarDado = input("\nDeseja lançar o dado s/n: ").lower()
    if jogarDado == "s":
        dado = random.randint(1,6)
        print (dado)
    elif jogarDado == "n":
        print ("\nPrograma encerrado")
        break
    else:
        print ("\nValor informado inválido")