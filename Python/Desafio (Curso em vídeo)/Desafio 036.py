print ("| EMPRÉSTIMO BANCÁRIO |")

valorCasa = float(input("Valor da casa: "))
salario = float(input("Salário mensal: "))
tempo = int(input("Deseja pagar em quantos anos? "))

mensalidade = (valorCasa/(tempo*12))

if mensalidade > (salario * 0.3):
    print (
        "\nEMPRÉSTIMO NEGADO. "
        "\nValor de Parcela: R${:.2f} "
        "\n30% DO SALÁRIO: R${:.2f} "
        "\nVALOR DE PARCELA MAIOR QUE 30% DO SALÁRIO!"
        .format(mensalidade,(salario*0.3)))
else:
    print (
        "\nEMPRÉSTIMO ACEITO! "
        "R${} = {}x de R${:.2f}".format(valorCasa,(tempo*12),mensalidade)
        )
