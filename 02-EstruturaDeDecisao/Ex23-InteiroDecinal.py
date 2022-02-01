""" 
   Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
   Dica: utilize uma função de arredondamento.

    @author Arthur
"""

numero = float(input("Digite o número: "))

if numero - int(numero) == 0:
   print("Número inteiro")
else:
   print("Número decimal")
