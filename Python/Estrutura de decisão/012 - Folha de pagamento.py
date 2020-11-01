print ("| FOLHA DE PAGAMENTO |")
print ()
print ()

#Declaração de variáveis
impRenda = 0
sind = 3
fgts = 11
salarioBruto = 0
salarioLiq = 0

#Salário bruto
valorHora = float(input("Valor pago por hora: "))
qtdTrab = float(input("Horas trabalhadas: "))
salarioBruto = (valorHora * qtdTrab)
print ()

#Condicionais impRenda
if salarioBruto <= 900:
    impRenda = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    impRenda = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    impRenda = 10
elif salarioBruto > 2500:
    impRenda = 20
else:
    print ("ERRO EM IMP. RENDA")

#Descontos
impRendaNovo = (impRenda * salarioBruto)/100
sindNovo = (sind * salarioBruto)/100
fgtsNovo = (fgts * salarioBruto)/100
desconto = (impRendaNovo + sindNovo)
salarioLiq = (salarioBruto - desconto)

#Saída
print ("Salário Bruto: (R$%.2f * %dh)..........: R$%.2f" % (valorHora,qtdTrab,salarioBruto))
print ("(-) IR (%d%%)..........................: R$%.2f" % (impRenda, impRendaNovo))
print ("(-) sind (%d%%)........................: R$%.2f" % (sind, sindNovo))
print ("FGTS (%d%%)............................: R$%.2f" % (fgts, fgtsNovo))
print ("Total de descontos.....................: R$%.2f" % (desconto))
print ("Salário Líquido........................: R$%.2f" % (salarioLiq))

input ()
