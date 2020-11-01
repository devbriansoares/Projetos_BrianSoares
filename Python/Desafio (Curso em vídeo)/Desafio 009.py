n = int(input("Informe um número inteiro: "))
mult = 0
result = 0
while mult <= 10:
    result = (n*mult)
    print ("{} x {} = {}".format(n,mult,result))
    mult += 1