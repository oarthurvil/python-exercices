""" 
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
    da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
    latas de tinta a serem compradas e o preço total.

    @author Arthur
"""

import math

metros_quadrados = float(input("Digite quantos metros quadrados serão pintados: "))

litros_tinta_necessarios = metros_quadrados / 3

latas_tinta_necessarias = litros_tinta_necessarios / 18
valor_total_real = latas_tinta_necessarias * 80

latas_tinta_fechadas = math.ceil(latas_tinta_necessarias)
valor_total_latas = latas_tinta_fechadas * 80

print("Quantidade de latas real: {}".format(round(latas_tinta_necessarias, 2)))
print("Preço total real: $ {}".format(round(valor_total_real, 2)))

print("Quantidade de latas fechadas: {}".format(latas_tinta_fechadas))
print("Preço total das latas: $ {}".format(valor_total_latas))