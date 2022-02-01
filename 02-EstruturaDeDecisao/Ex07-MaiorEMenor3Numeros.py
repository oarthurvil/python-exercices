""" 
   Faça um Programa que leia três números e mostre o maior e o menor deles.

    @author Arthur
"""

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

if num1 > num2 and num1 > num3:
    print("O maior entre {} {} {} é {}".format(num1, num2, num3, num1))
elif num2 > num1 and num2 > num3:
    print("O maior entre {} {} {} é {}".format(num1, num2, num3, num2))
else:
    print("O maior entre {} {} {} é {}".format(num1, num2, num3, num3))

if num1 < num2 and num1 < num3:
    print("O menor entre {} {} {} é {}".format(num1, num2, num3, num1))
elif num2 < num1 and num2 < num3:
    print("O menor entre {} {} {} é {}".format(num1, num2, num3, num2))
else:
    print("O menor entre {} {} {} é {}".format(num1, num2, num3, num3))