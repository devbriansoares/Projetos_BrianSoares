print ("| LOJA DE TINTAS 2 |")
print ()

qtdLata = 18
qtdGalao = 3.6
precoLata = 80
precoGalao = 25

metros = float(input("Informe o tamanho da área a ser pintada (em m²): "))

print ()
print ()

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

print ()
print ("Comprando apenas Latas de 18L: ",latasCompradas,"lata(s)")
print ("Valor total: R$","%.2f" % valorTotalLata)
print ()
print ("Comprando apenas Galões de 3.6L: ",galoesComprados,"galão(ões)")
print ("Valor total: R$","%.2f" % valorTotalGalao)
print ()
print ()

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


print ("MELHOR FORMA DE ECONOMIZAR (Lata + Galão")
print ("(QUANTIDADE SOLICITADA + 10%)")
print ()
print ("Latas 18L: ", latasCompradas2,"lata(s) +")
print ("Galões 3.6L: ", galoesComprados2,"galão(ões)")
print ("Valor Total: R$","%.2f" % NovoValorTotal)


input()
