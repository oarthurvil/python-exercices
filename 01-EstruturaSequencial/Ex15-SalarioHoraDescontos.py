""" 
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    
        -salário bruto.
        -quanto pagou ao INSS.
        -quanto pagou ao sindicato.
        -o salário líquido.
        -calcule os descontos e o salário líquido

    @author Arthur
"""

salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = int(input("Digite quantas horas você trabalhou: "))

salario_mes = salario_hora * horas_trabalhadas

imposto_renda = salario_mes * 0.11
inss = salario_mes * 0.08
sindicato = salario_mes * 0.05

total_impostos = imposto_renda + inss + sindicato

salario_liquido = salario_mes - total_impostos


print("Salário Bruto : $ {}".format(salario_mes))
print("IR : $ {}".format(imposto_renda))
print("INSS : $ {}".format(inss))
print("Sindicato : $ {}".format(sindicato))
print("Salário Liquido : $ {}".format(salario_liquido))