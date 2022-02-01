""" 
   Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
   O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
   nas seguintes situações:

      1 - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não 
      deve fazer pedir os demais valores, sendo encerrado;
      2 - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e
      encerre o programa;
      3 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
      4 - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

    @author Arthur
"""
import math

valor_a = float(input("Digite o valor de a: "))

if valor_a == 0:
   print("Não é uma operação de 2º grau")
   exit() 

valor_b = float(input("Digite o valor de b: ")) 
valor_c = float(input("Digite o valor de c: ")) 


delta = (valor_b ** 2) - 4 * (valor_a) * (valor_c)
formula_positiva = ((-valor_b) + math.sqrt(delta)) / (2 * valor_a)
formula_negativa = ((-valor_b) - math.sqrt(delta)) / (2 * valor_a)

if delta < 0:
   print("A equação não possui raízes reais")
   exit()
elif delta == 0:
   print("Resultado da equação: {}".format(formula_positiva))
elif delta > 0:
   print("Resultados da equação: {} e {}".format(formula_positiva, formula_negativa))
