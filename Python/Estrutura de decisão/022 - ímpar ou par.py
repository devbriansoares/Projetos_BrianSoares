print ("| ÍMPAR OU PAR |")

num = int(input("\nInforme um número inteiro: "))
if num % 2 == 0:
    print ("{} é um número par.".format(num))
else:
    print ("{} é um número ímpar.".format(num))