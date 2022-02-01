""" 
   Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor 
   do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis 
   serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
   O programa não deve se preocupar com a quantidade de notas existentes na máquina.

   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
   uma nota de 50, uma nota de 5 e uma nota de 1;

   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
   uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

    @author Arthur
"""

saque = int(input("Digite o valor do saque: "))

nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0

valor = saque

if valor >= 100:
   nota_100 = int(valor / 100)
   valor -= (nota_100 * 100) 

if valor < 100 and valor >= 50:
   nota_50 = int(valor / 50)
   valor -= (nota_50 * 50)

if valor < 50 and valor >= 10:
   nota_10 = int(valor / 10)
   valor -= (nota_10 * 10)

if valor < 10 and valor >= 5:
   nota_5 = int(valor / 5)
   valor -= (nota_5 * 5)
   
if valor < 5 and valor >= 1:
   nota_1 = int(valor / 1)
   valor -= (nota_1 * 1)

print("Notas de 100: {}".format(nota_100))
print("Notas de 50: {}".format(nota_50))
print("Notas de 10: {}".format(nota_10))
print("Notas de 5: {}".format(nota_5))
print("Notas de 1: {}".format(nota_1))