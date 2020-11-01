num = input("Insira um número entre 0 e 9999: ")
qtdLetras = len(num)
if qtdLetras == 1:
    print ("Unidade (s): {}".format(num))
elif qtdLetras == 2:
    print (" Unidade (s): {}\n Dezena (s): {}".format(num[1],num[0]))
elif qtdLetras == 3:
    print (" Unidade (s): {}\n Dezena (s): {}\n Centena (s): {}".format(num[2],num[1],num[0]))
elif qtdLetras == 4:
    print (" Unidade (s): {}\n Dezena (s): {}\n Centena (s): {}\n Milhar: {}".format(num[3],num[2],num[1],num[0]))
else:
    print ("Valor diferente do solicitado!")