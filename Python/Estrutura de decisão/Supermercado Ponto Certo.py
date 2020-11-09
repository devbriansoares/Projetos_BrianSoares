print ("| SEXTA DA CARNE |")

print ('''
                    Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 5,80 por Kg          R$ 4,90 por Kg
Alcatra         R$ 6,80 por Kg          R$ 5,90 por Kg
Picanha         R$ 7,80 por Kg          R$ 6,90 por Kg
''')

tipoCarne = input("Qual carne você vai levar? ").title()
qtdCarne = float(input("Quantos kg? "))
valorTotal = 0
print (tipoCarne)
if tipoCarne == "File Duplo":
    if qtdCarne > 5:
        valorTotal = qtdCarne * 4.90
    else:
        valorTotal = qtdCarne * 5.80
elif tipoCarne == "Alcatra":
    if qtdCarne > 5:
        valorTotal = qtdCarne * 5.90
    else:
        valorTotal = qtdCarne * 6.80
elif tipoCarne == "Picanha":
    if qtdCarne > 5:
        valorTotal = qtdCarne * 6.90
    else:
        valorTotal = qtdCarne * 7.80

formaPag = input("Forma de Pagamento - Cartão (C) / Dinheiro (D): ").upper()
if formaPag == "C":
    valorTotal = valorTotal - (valorTotal*0.05)
    print ('''
            SUPERMERCADO PONTO CERTO
Rua Barão de Moreno, 119. Vila Rica - Jaboatão dos Guararapes/PE
----------------------------------------------------------------
09/11/20 11:02:35                               CONTROLE: 000001
----------------------------------------------------------------
ID    CÓDIGO    DESCRIÇÃO       QTDE    UN          V. TOTAL
001    0000     {}         {:.2f}    Kg          R${:.2f}
----------------------------------------------------------------
DESCONTO  R$                                          R${:.2f}
VALOR TOTAL R$                                        R${:.2f}
FORMA DE PAGAMENTO: CARTÃO
'''.format(tipoCarne,qtdCarne,valorTotal,valorTotal*0.05,valorTotal))
elif formaPag == "D":
    print ('''
            SUPERMERCADO PONTO CERTO
Rua Barão de Moreno, 119. Vila Rica - Jaboatão dos Guararapes/PE
----------------------------------------------------------------
09/11/20 11:02:35                               CONTROLE: 000001
----------------------------------------------------------------
ID    CÓDIGO    DESCRIÇÃO       QTDE    UN          V. TOTAL
001    0000     {}         {:.2f}    Kg          R${:.2f}
----------------------------------------------------------------
DESCONTO  R$                                          R$0,00
VALOR TOTAL R$                                        R${:.2f}
FORMA DE PAGAMENTO: DINHEIRO
'''.format(tipoCarne,qtdCarne,valorTotal,valorTotal))
else:
    print ("Valor de entrada inválido!")