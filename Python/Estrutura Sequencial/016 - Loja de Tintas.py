print ("| LOJA DE TINTAS |")
print ()

precoLata = 80

metros = float(input("Informe o tamanho da área a ser pintada (em m²): "))

print ()
print ()

litros = int(metros / 3)
if litros % 18 == 0:
    latasCompradas = litros//18
else:
    latasCompradas = (litros//18) + 1

valorTotal = (latasCompradas * precoLata)

print ("Quantidade necessária: ",latasCompradas,"lata(s)")
print ("Preço total: R$","%.2f" % valorTotal)

input()
