print ("| TRIÂNGULO |")
print ()
print ()

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))
print ()

if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print ("Valor inválido")
else:
    if (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1:
        print ("Os valores informados não formam um triângulo")
    elif lado1 == lado2 and lado1 == lado3:
        print ("TRIÂNGULO EQUILÁTERO")
    elif lado1 == lado2 and lado1 != lado3:
        print ("TRIÂNGULO ISÓSCELES")
    elif lado2 == lado3 and lado1 != lado3:
        print ("TRIÂNGULO ISÓSCELES")
    elif lado3 == lado1 and lado3 != lado2:
        print ("TRIÂNGULO ISÓSCELES")
    elif lado1 != lado2 and lado1 != lado3:
        print ("TRIÂNGULO ESCALENO")
    else:
        print ("Erro no triângulo")
        

input ()
