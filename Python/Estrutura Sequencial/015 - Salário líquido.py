impRenda = 11
inss = 8
sind = 5

salarioHora = float(input("Informe quanto você recebe por hora trabalhada: "))
horaTrab = float(input("Informe quantas horas você trabalhou no mês: "))

salarioBruto = (salarioHora*horaTrab)
impRendaValor = (salarioBruto * (impRenda/100)) 
inssValor = (salarioBruto* (inss/100))
sindValor = (salarioBruto * (sind/100)) 
descontos = (impRendaValor+inssValor+sindValor)
salarioLiq = (salarioBruto-descontos)

print ("\nSalário bruto: R${:.2f}".format(salarioBruto))
print ("Quanto pagou de INSS: R${:.2f}".format(inssValor))
print ("Quanto pagou ao sindicato: R${:.2f}".format(sindValor))
print ("Salário Líquido: R${:.2f}".format(salarioLiq))