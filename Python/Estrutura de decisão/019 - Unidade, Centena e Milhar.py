print ("| UNIDADE, CENTENA E MILHAR |")

num = input("Insira um número entre 0 e 9999: ")
qtdLetras = len(num)
if qtdLetras == 1:
    print ("{} = {} Unidade(s).".format(num,num))
elif qtdLetras == 2:
    print ("{} = {} Dezena(s), {} unidade(s).".format(num,num[0],num[1]))
elif qtdLetras == 3:
    print ("{} = {} Centena(s), {} dezena(s) e {} unidade(s).".format(num,num[0],num[1],num[2]))
elif qtdLetras == 4:
    print ("{} = {} Milhar(es), {} Centena(s), {} dezena(s) e {} unidade(s).".format(num, num[0],num[1],num[2],num[3]))
else:
    print ("Valor diferente do solicitado!")