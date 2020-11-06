print ("| ALISTAMENTO |")

idade = float(input("\nQUAL A SUA IDADE? "))

if idade < 18:
    print ("Falta(m) {} ano(s) para seu alistamento.".format(18-idade))
elif idade == 18:
    print ("Hora de servir à pátria!")
else:
    print ("Passou {} ano(s) do seu alistamento.".format(idade-18))