import random

nomes = ["Brian","Lucas","Aquiles","Igor","Irineu"]
generos = ["Animação","Comédia","Ação","Terror"]

positionNome = random.choice(nomes)
positionGenero = random.choice(generos)
print ("O escolhido foi: {} com o gênero {}".format(positionNome,positionGenero))