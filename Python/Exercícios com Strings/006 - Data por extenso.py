data = input("Data: ").split("/")
mes = 1
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
while True:
    print (data[1])
    if data[1] == mes:
        print ("Você nasceu em {} de {} de {}".format(data[0],meses[mes],data[2]))
        break
    else:
        mes += 1