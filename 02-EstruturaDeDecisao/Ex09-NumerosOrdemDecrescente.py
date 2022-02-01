""" 
   Faça um Programa que leia três números e mostre-os em ordem decrescente.

    @author Arthur
"""

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))


# num1 > num2 > num3
if num1 > num2 and num1 > num3 and num2 > num3:
    print("Ordem decrescente {} > {} > {}".format(num1, num2, num3))

# num1 > num3 > num2
elif num1 > num2 and num1 > num3 and num3 > num2:
   print("Ordem decrescente {} > {} > {}".format(num1, num3, num3))

# num2 > num1 > num3
elif num2 > num1 and num2 > num3 and num1 > num3:
   print("Ordem decrescente {} > {} > {}".format(num2, num1, num3))

# num2 > num3 > num1
elif num2 > num1 and num2 > num3 and num3 > num1:
   print("Ordem decrescente {} > {} > {}".format(num1, num3, num3))

# num3 > num1 > num2
elif num3 > num1 and num3 > num2 and num1 > num2:
   print("Ordem decrescente {} > {} > {}".format(num3, num1, num2))

# num3 > num2 > num1
elif num3 > num1 and num3 > num2 and num2 > num1:
   print("Ordem decrescente {} > {} > {}".format(num3, num2, num1))