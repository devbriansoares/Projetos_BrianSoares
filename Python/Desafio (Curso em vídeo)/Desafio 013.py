salario = float(input("Informe seu salário: "))
aumento = 15
salarioNovo = (salario+(salario*(aumento/100)))

print ("Salário novo com aumento de {}% é R${:.2f}.".format (aumento,salarioNovo))