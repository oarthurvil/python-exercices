""" 
   Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    @author Arthur
"""

entrada_dia = int(input("Digite o dia: "))
entrada_mes = int(input("Digite o mês: "))
entrada_ano = int(input("Digite o ano: "))


dia = False
mes = False
ano = False

if entrada_dia > 0 and entrada_dia <= 31:
   dia = True

if entrada_mes > 0 and entrada_mes <= 12:
   mes = True

if entrada_ano > 0:
   ano = True


if dia and mes and ano:
   print("{}/{}/{}".format(entrada_dia, entrada_mes, entrada_ano))
else:
   print("Digite valores válidos.")



