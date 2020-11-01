print ("| ORGANIZAÇOES TABAJARA |")
print ()

aumento = 0
percAumento = 0
salario = float(input("Informe o salário: "))
print ()
print ()

if salario <= 280 and salario > 0:
    salarioNovo = salario + (salario * 0.20)
    percAumento = 20
    aumento = salario * 0.20
elif salario > 280 and salario <= 700:
    salarioNovo = salario + (salario * 0.15)
    percAumento = 15
    aumento = salario * 0.15
elif salario > 700 and salario < 1500:
    salarioNovo = salario + (salario * 0.10)
    percAumento = 10
    aumento = salario * 0.10
elif salario >= 1500:
    salarioNovo = salario (salario * 0.05)
    percAumento = 5
    aumento = salario * 0.05
else:
    print ("Valor inválido")



print ("Salário antes do ajuste: R$","%.2f" % salario)
print ("Percentual de aumento aplicado:", percAumento,"%")
print ("Valor do aumento: R$","%.2f" % aumento)
print ("Novo salário: R$","%.2f" % salarioNovo)

input()
