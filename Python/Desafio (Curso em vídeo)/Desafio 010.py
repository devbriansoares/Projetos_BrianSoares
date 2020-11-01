real = float(input("Informe um valor em R$: "))
dolar = 5.62
result = (real/dolar)

print ("Com R${:.2f} você pode comprar US${:.2f}.".format (real,result))