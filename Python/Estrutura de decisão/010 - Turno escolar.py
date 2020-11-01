print ("| TURNO ESCOLAR |")
print ()

print ("(M) MATUTINO / (V) VESPERTINO / (N) NOTURNO ")
turno = input("Turno escolar (M/V/N): ")
turno = turno.upper()
print ()

if turno == "M":
    print ("Bom dia!")
elif turno == "V":
    print ("Boa tarde!")
elif turno == "N":
    print ("Boa noite!")
else:
    print ("Valor inválido.")  

    

input()
