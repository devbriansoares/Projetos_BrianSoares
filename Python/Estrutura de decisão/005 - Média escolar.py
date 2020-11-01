print ("| MÉDIA ESCOLAR |")
print ()
print("DIGITE 2 NOTAS PARCIAIS PARA CALCULAR A MÉDIA (0 A 10)")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = ((n1+n2)/2)
print ()

if n1 < 0 or n1 > 10:
    print ("Erro na entrada de dados!")
elif n2 < 0 or n2 > 10:
    print ("Erro na entrada de dados!")
elif media == 10:
    print ("APROVADO COM DISTINÇÃO! PARABÉNS!!!")
elif media >= 7 and media < 10:
    print ("APROVADO!")
elif media >= 0 and media < 7:
    print ("REPROVADO!")
else:
    print ("Erro na entrada de dados!")


input()
