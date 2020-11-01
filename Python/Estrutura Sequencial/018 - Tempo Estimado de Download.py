print ("| TEMPO ESTIMADO DE DOWNLOAD |")
print ()

tamanho = float(input("Informe o tamanho do arquivo (Mb): "))
velocidade = float(input("Informe a velocidade da internet (Mbps): "))

tempo = ((tamanho/velocidade)/60)

print ()
print ("Tempo de download:","%.1f" % tempo,"min")

input()
