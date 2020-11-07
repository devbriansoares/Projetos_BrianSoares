print ("| INTEIRO OU DECIMAL? |")

num = float(input("\nInforme um número real: "))
if (round(num) - num) == 0:
    print ("{} é um número inteiro.".format(num))
else:
    print ("{} é um número decimal".format(num))