print ("| MASCULINO OU FEMININO |")
print ()

print ("(M) MASCULINO / (F) FEMININO")
sexo = input("Sexo (M/F): ")
sexo = sexo.upper()
print ()
if sexo == "M":
    print ("Sexo informado: Masculino.")
elif sexo == "F":
    print ("Sexo informado: Feminino.")
else:
    print ("Sexo inválido.")


input()
