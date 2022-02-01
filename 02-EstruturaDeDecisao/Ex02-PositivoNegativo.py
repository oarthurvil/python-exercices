""" 
    Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

    @author Arthur
"""

num = float(input("Digite um número: "))

if num > 0:
    print("O {} é positivo".format(num))
elif num < 0:
    print("O {} é negativo".format(num))
else:
    print("O {} é zero".format(num))