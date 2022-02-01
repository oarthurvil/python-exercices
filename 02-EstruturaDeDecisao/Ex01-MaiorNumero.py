""" 
    Faça um Programa que peça dois números e imprima o maior deles.

    @author Arthur
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O {} é maior que {}".format(num1, num2))
else:
    print("O {} é maior que {}".format(num2, num1))