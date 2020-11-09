while True:
    nome = input("\nNome: ").title()
    if len(nome) > 3:
        idade = int(input("Idade: "))
        if idade > 0 and idade <= 150:
            salario = float(input("Salário: "))
            if salario > 0:
                sexo = input("Sexo M/F: ").upper()
                if sexo == "M" or sexo == "F":
                    estadoCivil = input("Estado Civil S/C/V/D: ").upper()
                    if estadoCivil in ["S","C","V","D"]:
                        break
print ('''
Nome: {}
Idade: {}
Salário: R${:.2f}
sexo: {}
Estado Civil: {}'''.format(nome,idade,salario,sexo,estadoCivil))