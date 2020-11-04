# Faça um programa para uma loja de tintas. O programa deverá 
# pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 
# 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas 
# de tinta a serem compradas e o preço total.
precoLata = 80

metros = float(input("Informe o tamanho da área a ser pintada (em m²): "))

litros = int(metros / 3)
if litros % 18 == 0:
    latasCompradas = litros//18
else:
    latasCompradas = (litros//18) + 1

valorTotal = (latasCompradas * precoLata)

print ("\nQuantidade necessária: {} latas(s)".format(latasCompradas))
print ("Preço total: R${:.2f}".format(valorTotal))