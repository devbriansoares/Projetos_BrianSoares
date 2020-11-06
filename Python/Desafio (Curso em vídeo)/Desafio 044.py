print ("| FORMA DE PAGAMENTO |")

valor = float(input("Valor do produto: "))
print ("\nFORMA DE PAGAMENTO"
       "\nDigite 1 para pagamentos à vista em dinheiro/cheque"
       "\nDigite 2 para pagamentos à vista em cartão"
       "\nDigite 3 para pagamentos em até 2x no cartão"
       "\nDigite 4 para pagamento em 3x ou mais no cartão (c/ Juros)"
        )
formaPag = int(input("\nForma de pagamento: "))
if formaPag == 1:
    valor = valor - (valor*0.10)
    print ("\nValor a ser pago: R${:.2f}".format(valor))
    print ("Condição de pagamento: À vista em dinheiro/cheque.")
elif formaPag == 2:
    valor = valor - (valor*0.05)
    print ("\nValor a ser pago: R${:.2f}".format(valor))
    print ("Condição de pagamento: À vista em cartão.")
elif formaPag == 3:
    print ("Valor a ser pago: R${:.2f}".format(valor))
    print ("Condição de pagamento: Até 2x no cartão.")
elif formaPag == 4:
    valor = valor + (valor*0.20)
    print ("Valor a ser pago: R${:.2f}".format(valor))
    print ("Condição de pagamento: Em 3x ou mais no cartão.")
else:
    print ("Você inseriu uma forma de pagamento inválida!")