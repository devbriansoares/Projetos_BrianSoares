print ("| CÁLCULO DE SALÁRIO LÍQUIDO |")
print ()

impRenda = 11
inss = 8
sind = 5

salarioHora = float(input("Informe quanto você recebe por hora trabalhada: "))
horaTrab = float(input("Informe quantas horas você trabalhou no mês: "))
print ()
print ()

salarioBruto = (salarioHora*horaTrab)
impRendaValor = (salarioBruto * (impRenda/100)) 
inssValor = (salarioBruto* (inss/100))
sindValor = (salarioBruto * (sind/100)) 
descontos = (impRendaValor+inssValor+sindValor)
salarioLiq = (salarioBruto-descontos)

print ("Salário bruto: R$","%.2f" % salarioBruto)
print ("Quanto pagou de INSS: R$","%.2f" % inssValor)
print ("Quanto pagou ao sindicato: R$","%.2f" % sindValor)
print ("Salário Líquido: R$","%.2f" % salarioLiq)



input()
