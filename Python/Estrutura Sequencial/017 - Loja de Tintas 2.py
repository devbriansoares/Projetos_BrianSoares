print ("| LOJA DE TINTAS 2 |")

qtdLata = 18
qtdGalao = 3.6
precoLata = 80
precoGalao = 25

metros = float(input("\nInforme o tamanho da área a ser pintada (em m²): "))

litros = float(metros / 6)
if litros % qtdLata == 0:
    latasCompradas = litros//18
elif litros % qtdGalao == 0:
    galoesComprados = litros//3.6
else:
    latasCompradas = (litros//qtdLata) + 1
    galoesComprados = (litros//qtdGalao) + 1

valorTotalLata = (latasCompradas * precoLata)
valorTotalGalao = (galoesComprados * precoGalao)

print ("\nComprando apenas Latas de 18L: {} lata(s)".format(latasCompradas))
print ("Valor total: R${:.2f}".format(valorTotalLata))

print ("\nComprando apenas Galões de 3.6L: {} galão(ões)".format(galoesComprados))
print ("Valor total: R${:.2f}".format(valorTotalGalao))

#Arredondamento
qtdArredondada = litros + (litros * 0.10)
restoLata = (qtdArredondada % qtdLata)
latasCompradas2 = latasCompradas
galoesComprados2 = galoesComprados

if restoLata >= qtdGalao:
    latasCompradas2 = qtdArredondada // qtdLata
    if restoLata % qtdGalao == 0:
        galoesComprados2 = (restoLata//3.6)
    else:
        galoesComprados2 = (restoLata//qtdGalao) + 1
else:
    if restoLata == 0:
        galoesComprados2 = 0
    else:
        galoesComprados2 = 1

NovoValorTotal = ((latasCompradas2 * precoLata) + (galoesComprados2 * precoGalao))

print ("\nMELHOR FORMA DE ECONOMIZAR (Lata + Galão)")
print ("|----- QUANTIDADE SOLICITADA + 10% -----|")
print ("\nLatas 18L: {} lata(s) +".format(latasCompradas2))
print ("Galões 3.6L: {} galão(ões)".format(galoesComprados2))
print ("Valor Total: R${:.2f}".format(NovoValorTotal))