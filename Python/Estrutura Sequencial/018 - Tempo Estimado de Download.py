tamanho = float(input("Informe o tamanho do arquivo (Mb): "))
velocidade = float(input("Informe a velocidade da internet (Mbps): "))

tempo = ((tamanho/velocidade)/60)

print ("\nTempo de download: {:.1f}min".format(tempo))