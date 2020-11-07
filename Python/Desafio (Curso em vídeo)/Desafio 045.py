import random
print ("| JOKENPÔ |")

pcMao = ["pedra","papel","tesoura"]
pcJogada = ""
pcScore = 0
playerScore = 0
while True:
    print ("\n| PC  {} x  {} PLAYER |".format(pcScore,playerScore))
    pcJogada = random.choice(pcMao)

    minhaMao = input("\nPedra, papel ou tesoura? ").lower()
    if pcJogada == minhaMao:
        print ("{} = {}. EMPATE!".format(pcJogada,minhaMao))
    elif pcJogada == "pedra":
        if minhaMao == "papel":
            print ("{} perde pra {}. VOCÊ VENCEU!".format(pcJogada,minhaMao))
            playerScore += 1
        elif minhaMao == "tesoura":
            print ("{} ganha pra {}. VOCÊ PERDEU!".format(pcJogada,minhaMao))
            pcScore += 1
    elif pcJogada == "papel":
        if minhaMao == "pedra":
            print ("{} ganha de {}. VOCÊ PERDEU!".format(pcJogada,minhaMao))
            pcScore += 1
        elif minhaMao == "tesoura":
            print ("{} perde pra {}. VOCÊ VENCEU!".format(pcJogada,minhaMao))
            playerScore += 1
    elif pcJogada == "tesoura":
        if minhaMao == "pedra":
            print ("{} perde pra {}. VOCÊ VENCEU!".format(pcJogada,minhaMao))
            playerScore += 1
        elif minhaMao == "papel":
            print ("{} ganha pra {}. VOCÊ PERDEU!".format(pcJogada,minhaMao))
            pcScore += 1
    if pcScore == 5:
        print ("\n----------PC VENCEU!!!----------")
        break
    elif playerScore == 5:
        print ("\n----------VOCÊ VENCEU!!!----------")
        break