""" 
   Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
   O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

   par ou ímpar;
   positivo ou negativo;
   inteiro ou decimal.

    @author Arthur
"""
print("Calculadora")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

entrada_operacao = input("Digite a operação \n(SOM) soma\n(SUB) subtração\n(MULT) multiplicação\n(DIV) divisão\n")

operacao = entrada_operacao.upper()

numero = 0

if operacao == "SOM":
   numero = num1 + num2
elif operacao == "SUB":
   numero = num1 - num2
elif operacao == "MULT":
   numero = num1 * num2
elif operacao == "DIV":
   numero = num1 / num2
else:
   print("Operação inválida")
   exit()


if numero % 2 == 0:
   print("{} é par".format(numero))
else:
   print("{} é ímpar".format(numero))

if numero > 0:
    print("{} é positivo".format(numero))
elif numero < 0:
    print("{} é negativo".format(numero))
else:
    print("{} é zero".format(numero))

if numero - int(numero) == 0:
   print("{} é inteiro".format(numero))
else:
   print("{} é decimal".format(numero))
