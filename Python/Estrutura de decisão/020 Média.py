print ("| MÉDIA ESCOLAR |")
print ()

notas = [0,0,0]
x = 0
while x < 3:
    notas[x] = float(input("Nota {}: ".format(x+1)))
    x +=1
x = 0
total = 0
while x < 3:
    total += notas[x]
    x += 1

media = total/len(notas)
if media == 10:
    print ("APROVADO COM DISTINÇÃO! MÉDIA {:.1f}.".format(media))
elif media >= 7:
    print ("APROVADO! MÉDIA: {:.1f}.".format(media))
else:
    print ("REPROVADO! MÉDIA: {:.1f}.".format(media))