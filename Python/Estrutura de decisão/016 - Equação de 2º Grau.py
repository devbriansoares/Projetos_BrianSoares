print ("| EQUAÇÃO DE 2º GRAU |")
print ()
print ()

a = 0
b = 0
c = 0
x = 0
a = float(input("Valor de a: "))

if a == 0:
    print ("A equação não é do 2º Grau.")
else:
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    delta = ((b**2) - 4*(a*c))
    if delta < 0:
        print ("A equação não possui raizes reais.")
    elif delta == 0:
        x = ((-b + (delta ** 0.5))/(2*a))
        print ("A equação possui apenas uma raiz real.")
        print ("Valor da raiz: %.2f" % (x))
    elif delta > 0:
        x = ((-b + (delta ** 0.5))/(2*a))
        x2 = ((-b - (delta ** 0.5))/(2*a))
        print ("A equação possui duas raízes reais.")
        print ("Valor das raízes: %.1f e %.1f" % (x, x2))

input ()
