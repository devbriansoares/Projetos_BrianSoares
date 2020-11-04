#Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total
#do seu salário no referido mês.

salarioHora = float(input("Salário por hora: "))
horaTrab = float(input("Horas trabalhadas no mês: "))
salarioMes = (salarioHora*horaTrab)

print ("\nSalário mensal = R${}%.2f".format (salarioMes))