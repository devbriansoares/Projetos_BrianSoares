print ("| CENA DE CRIME |")
print ("\nRESPONDA COM 'S' PARA SIM OU 'N' PARA NÃO")

perguntas = []

q1 = input("\nTelefonou para a vítima? ").upper()
q2 = input("Esteve no local do crime? ").upper()
q3 = input("Mora perto da vítima? ").upper()
q4 = input("Devia para a vítima? ").upper()
q5 = input("Já trabalhou com a vítima? ").upper()

perguntas.append(q1)
perguntas.append(q2)
perguntas.append(q3)
perguntas.append(q4)
perguntas.append(q5)

if perguntas.count("S") == 5:
    print ("\nASSASSINO!")
elif perguntas.count("S") >= 3 and perguntas.count("S") < 5:
    print ("\nCÚMPLICE!")
elif perguntas.count("S") == 2:
    print ("\nSUSPEITA!")
else:
    print ("\nINOCENTE!")