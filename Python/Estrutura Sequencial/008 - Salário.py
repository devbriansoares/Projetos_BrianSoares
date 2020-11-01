print ("| SALÁRIO |")
print ()
salarioHora = float(input("Salário por hora: "))
horaTrab = float(input("Horas trabalhadas no mês: "))
salarioMes = (salarioHora*horaTrab)

print ()
print ("Salário mensal = R$","%.2f" % salarioMes)

input()
