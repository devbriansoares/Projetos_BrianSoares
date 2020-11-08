print ("| MASCULINO OU FEMININO |")
print ("\n(M) MASCULINO / (F) FEMININO")

sexo = input("Sexo (M/F): ").upper()

if sexo == "M":
    print ("Sexo informado: Masculino.")
elif sexo == "F":
    print ("Sexo informado: Feminino.")
else:
    print ("Sexo inválido.")