""" 
   As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram 
   para desenvolver o programa que calculará os reajustes.

   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
   seguinte critério, baseado no salário atual:

   salários até R$ 280,00 (incluindo) : aumento de 20%
   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
   o salário antes do reajuste;
   o percentual de aumento aplicado;
   o valor do aumento;
   o novo salário, após o aumento.

    @author Arthur
"""

salario = float(input("Digite o salário do colaborador: "))

if salario >= 280:
   reajuste = 20
   valor_reajuste = salario * (reajuste / 100)
   novo_salario = salario + valor_reajuste
   print("Salário de $ {} com reajuste de {} % correspondente ${}= $ {}".format(salario, reajuste, valor_reajuste, novo_salario))
elif salario > 280 and salario <= 700:
   reajuste = 15
   valor_reajuste = salario * (reajuste / 100)
   novo_salario = salario + valor_reajuste
   print("Salário de $ {} com reajuste de {} % correspondente ${}= $ {}".format(salario, reajuste, valor_reajuste, novo_salario))  
elif salario > 700 and salario <= 1500:
   reajuste = 10
   valor_reajuste = salario * (reajuste / 100)
   novo_salario = salario + valor_reajuste
   print("Salário de $ {} com reajuste de {} % correspondente ${}= $ {}".format(salario, reajuste, valor_reajuste, novo_salario))   
elif salario > 1500:
   reajuste = 5
   valor_reajuste = salario * (reajuste / 100)
   novo_salario = salario + valor_reajuste
   print("Salário de $ {} com reajuste de {} % correspondente ${}= $ {}".format(salario, reajuste, valor_reajuste, novo_salario))   