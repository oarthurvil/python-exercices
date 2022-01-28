""" 
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    - o produto do dobro do primeiro com metade do segundo .
    - a soma do triplo do primeiro com o terceiro.
    - o terceiro elevado ao cubo.

    @author Arthur
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

calc1 = (2 * num1) + (num2 / 2)
calc2 = (3 * num1) + num3
calc3 = num3**3

print("O produto do dobro de {} com metade do {} = {}".format(num1, num2, calc1))
print("A soma do triplo do {} com o {} = {}".format(num1, num3, calc2))
print("O {} elevado ao cubo = {}".format(num3, calc3))
