import random
print ("| CHUTE UM NÚMERO ENTRE 1 E 100 |")
print ()
print ()

nome = input("Seu nome: ").capitalize()

erroString = False
listaChute = []
n = random.randint(1,100)
print ()
while True:
    print ("Palpites: {}".format(listaChute))
    try:
        chute = int(input("Informe seu palpite: "))
        erroString = False
    except ValueError:
        erroString = True
        print ()
    if erroString == True:
        print ("----- INFORME UM NÚMERO ENTRE 1 E 100 -----")
    else:
        if chute in listaChute:
            print ("Palpite repetido!")        
        elif chute < 1 or chute > 100:
            print ("----- INFORME UM NÚMERO ENTRE 1 E 100 -----")
            print()
        else:
            if n == chute:
                print ("PARABÉNS, {}! VOCÊ ACERTOU!!!".format(nome))
                break
            elif n < chute:
                listaChute.append(chute)
                print ("Chutou alto! Tente outra vez!")
                print ()
            elif n > chute:
                listaChute.append(chute)
                print ("Chutou baixo! Tente outra vez!")
                print ()
            else:
                ()

input ()
