print ("| DATA VÁLIDA |")
print ()
print ()

erroData = ()
dia = int(input("Dia: "))
if dia < 1 or dia > 31:
    print ("Valor para dia inválido!")
else:
    mes = int(input("Mês: "))
    if mes < 1 or mes > 12:
        print ("Valor para mês inválido!")
    else:
        ano = int(input("Ano: "))
        if ano < 1:
            print ("Valor para ano inválido!")
        else:
            if ano % 4 != 0 or ano % 100 == 0:
                if mes == 2 and dia > 28:
                    erroData = True
                else:
                    ()
            else:
                ()
            print ()
            if erroData == True:
                print ("%d/%d/%d Não é uma data válida. Ano bissexto!" % (dia,mes,ano))
            else:
                print ("%d/%d/%d é uma data válida!" % (dia,mes,ano))


input ()
