""" 
   Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
   são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% 
   para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
   (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
   O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

      Desconto do IR:
      Salário Bruto até 900 (inclusive) - isento
      Salário Bruto até 1500 (inclusive) - desconto de 5%
      Salário Bruto até 2500 (inclusive) - desconto de 10%
      Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
      dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    @author Arthur
"""

valor_hora = float(input("Digite o valor da hora: "))
quant_horas = float(input("Digite quantas horas foram trabalhadas: "))

impost_ir = 0
impost_inss = 10
impost_fgts = 11 

salario_bruto =  valor_hora * quant_horas

if salario_bruto <= 900:
   impost_ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
   impost_ir = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
   impost_ir = 10
elif salario_bruto > 2500:
   impost_ir = 20

valor_ir = salario_bruto * (impost_ir / 100)
valor_inss = salario_bruto * (impost_inss / 100)
valor_fgts = salario_bruto * (impost_fgts / 100)

total_descontos = valor_ir + valor_inss
salario_liquido = salario_bruto - (valor_ir + valor_inss)

print("Salário bruto: {}".format(salario_bruto))
print("Imposto de renda {}%: {}".format(impost_ir, valor_ir))
print("INSS {}%: {}".format(impost_inss, valor_inss))
print("FGTS {}%: {}".format(impost_fgts, valor_fgts))
print("Total de descontos: {}".format(total_descontos))
print("Salário Líquido: {}".format(salario_liquido))
