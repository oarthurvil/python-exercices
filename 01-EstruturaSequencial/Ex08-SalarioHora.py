""" 
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês.

    @author Arthur
"""

salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = int(input("Digite quantas horas você trabalhou: "))

salario_mes = salario_hora * horas_trabalhadas

print("Para {} trabalhadas o salário total é {}".format(horas_trabalhadas, salario_mes))