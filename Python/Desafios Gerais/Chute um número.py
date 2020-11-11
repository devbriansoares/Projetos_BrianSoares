import random
print ("| CHUTE UM NÚMERO ENTRE 1 E 100 |")

nome = input("Seu nome: ").capitalize()

nome = input("\nSeu nome: ").upper()
erroString = False
listaChute = []
n = random.randint(1,100)

while True:
    print ("Palpites: {}".format(listaChute))
    try:
        chute = int(input("Informe seu palpite: "))
        erroString = False
    except ValueError:
        erroString = True
        print ()
    if erroString == True:
        print ("\n----- INFORME UM NÚMERO ENTRE 1 E 100 -----")
    else:
        if chute in listaChute:
            print ("Palpite repetido!")        
        elif chute < 1 or chute > 100:
            print ("\n----- INFORME UM NÚMERO ENTRE 1 E 100 -----")
        else:
            if n == chute:
                print ("\nPARABÉNS, {}! VOCÊ ACERTOU!!!".format(nome))
                break
            elif n < chute:
                listaChute.append(chute)
                print ("\nChutou alto! Tente outra vez!")
            elif n > chute:
                listaChute.append(chute)
                print ("\nChutou baixo! Tente outra vez!")
            else:
                ()