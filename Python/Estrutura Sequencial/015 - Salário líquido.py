# Faça um Programa que pergunte quanto você ganha por hora e 
# o número de horas trabalhadas no mês. Calcule e mostre o 
# total do seu salário no referido mês, sabendo-se que são 
# descontados 11% para o Imposto de Renda, 8% para o INSS e 
# 5% para o sindicato, faça um programa que nos dê:
# A) Salário bruto. /// B) Quanto pagou ao INSS.
# C) Quanto pagou ao sindicato /// D) O salário líquido.
# E) Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
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

print ("\nSalário bruto: R$","%.2f" % salarioBruto)
print ("Quanto pagou de INSS: R$","%.2f" % inssValor)
print ("Quanto pagou ao sindicato: R$","%.2f" % sindValor)
print ("Salário Líquido: R$","%.2f" % salarioLiq)