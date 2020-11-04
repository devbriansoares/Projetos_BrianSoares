# Faça um programa que peça o tamanho de um arquivo 
# para download (em MB) e a velocidade de um link 
# de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Informe o tamanho do arquivo (Mb): "))
velocidade = float(input("Informe a velocidade da internet (Mbps): "))

tempo = ((tamanho/velocidade)/60)

print ("\nTempo de download: {:.1f}min".format(tempo))