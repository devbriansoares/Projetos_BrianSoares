print ("| MÉDIA ESCOLAR COM CONCEITO |")
print ()
print ()

#média
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = ((nota1 + nota2)/2)
print ()

if nota1 < 0 or nota1 > 10:
    print ("Valor inválido")
elif nota2 < 0 or nota2 > 10:
    print ("Valor inválido")
else:
    #Conceito
    conceito = ""
    if media < 0 or media > 10:
        print ("Valor inválido")
    else:
        if media >= 9 and media <= 10:
            conceito = "A"
        elif media >= 7.5 and media < 9:
            conceito = "B"
        elif media >= 6 and media < 7.5:
            conceito = "C"
        elif media >= 4 and media < 6:
            conceito = "D"
        elif media >= 0 and media < 4:
            conceito = "E"
        else:
            print ("ERRO NO CONCEITO")

    #Status
    status = ""
    if conceito == "A" or conceito == "B" or conceito == "C":
        status = "APROVADO"
    elif conceito == "D" or conceito == "E":
        status = "REPROVADO"
    else:
        print ("Erro no status")

    print ("Nota Parcial 1:", nota1)
    print ("Nota parcial 2:", nota2)
    print ("Média de aproveitamento:", media)
    print ("Conceito:", conceito)
    print ("Status:", status)

input ()
