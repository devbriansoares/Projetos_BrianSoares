print ("| CAIXA ELETRÔNICO |")

valor = float(input("\nValor do saque: R$"))

if valor % 100 == 0:
    print ("{} nota(s) de R$100,00".format(valor//100))
elif valor % 100 > 0:
    print ("{} nota(s) de R$100,00".format(valor//100))
    valor = valor%100
    if valor == 50:
        print ("{} nota(s) de R$50,00".format(valor//50))
    elif valor % 50 > 0:
        print ("{} nota(s) de R$50,00".format(valor//50))
        valor = valor%50
        if valor % 10 == 0:
            print ("{} nota(s) de R$10,00".format(valor//10))
        elif valor % 10 > 0:
            print ("{} nota(s) de R$10,00".format(valor//10))
            valor = valor%10
            if valor % 5 == 0:
                print ("{} nota(s) de R$5,00".format(valor//5))
            elif valor % 5 > 0:
                print ("{} nota(s) de R$5,00"
                "\n{} nota(s) de R$1,00"
                .format(valor//5,valor%5))