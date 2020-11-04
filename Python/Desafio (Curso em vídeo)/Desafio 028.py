import random
print ("| JOGO DA ADIVINHAÇÃO |")
print ("\nCHUTE UM NÚMERO ENTRE 1 E 100")
print ("|--VOCÊ TEM 10 TENTATIVAS!--|")
nome = input("\nInforme seu nome: ").capitalize()
num = random.randint(1,100)

cont = 1
listaChute = []
errorInput = False
while True:
    print ("\nTENTATIVA NÚMERO: {}".format (cont))
    if cont == 11:
        print ("Que pena, {}! O número secreto é: {}".format (nome,num))
        break
    else:
        print ("\nPalpites: {}".format (listaChute))
        try:
            palpite = int(input("Informe seu palpite: "))
            errorInput = False
        except ValueError:
            errorInput = True
        if errorInput == True:
            print ("-----INFORME UM NÚMERO ENTRE 1 E 100-----")
        elif palpite < 1 or palpite > 100:
            print ("-----INFORME UM NÚMERO ENTRE 1 E 100-----")
        else:
            if palpite == num:
                print ("\n-----Parabéns, {}! Você acertou!!!-----".format(nome))
                break
            else:
                if palpite in listaChute:
                    print ("\nPalpite repetido!")
                elif palpite < num:
                    print ("Chutou baixo. Tente novamente!")
                    listaChute.append(palpite)
                    cont += 1
                elif palpite > num:
                    print ("Chutou alto. Tente novamente!")
                    listaChute.append(palpite)
                    cont += 1
        