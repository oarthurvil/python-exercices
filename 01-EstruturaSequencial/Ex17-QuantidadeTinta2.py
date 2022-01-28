""" 
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
    da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
    que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

        -comprar apenas latas de 18 litros;
        -comprar apenas galões de 3,6 litros;
        -misturar latas e galões, de forma que o desperdício de tinta seja menor. 
            Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
            considere latas cheias.

    @author Arthur
"""

import math


metros_quadrados = float(input("Digite quantos metros quadrados serão pintados: "))

litros_tinta_necessarios = metros_quadrados / 6

    #Valores decimais
latas_tinta_necessarias = litros_tinta_necessarios / 18
valor_total_real_latas = latas_tinta_necessarias * 80

galoes_tinta_necessarios = litros_tinta_necessarios / 3.6
valor_total_real_galoes = galoes_tinta_necessarios * 25


    #Valores inteiros
latas_tinta_fechadas = math.ceil(latas_tinta_necessarias)
valor_total_latas = latas_tinta_fechadas * 80

galoes_tinta_fechadas = math.ceil(galoes_tinta_necessarios)
valor_total_galoes = galoes_tinta_fechadas * 25

    #Valores inteiros Latas e galões
quant_latas = int(latas_tinta_necessarias)
quant_galoes = math.ceil(((latas_tinta_necessarias - quant_latas) * 10) / 3.6)

valor_latas = quant_latas * 80
valor_galoes = quant_galoes * 25
valor_total_latas_galoes = valor_latas + valor_galoes


    #Output valores decimais

print("Quantidade de latas real: {}".format(round(latas_tinta_necessarias, 2)))
print("Preço total real: $ {}".format(round(valor_total_real_latas, 2)))


print("Quantidade de galões real: {}".format(round(galoes_tinta_necessarios, 2)))
print("Preço total real: $ {}".format(round(valor_total_real_galoes, 2)))
print("\n")

    #Output valores inteiros
print("Quantidade de latas fechadas: {}".format(latas_tinta_fechadas))
print("Preço total das latas: $ {}".format(valor_total_latas))

print("Quantidade de galões fechados: {}".format(galoes_tinta_fechadas))
print("Preço total de galões: $ {}".format(valor_total_galoes))
print("\n")

    #Output valores inteiros latas e galões
print("Quantidade {} latas {} galões fechados".format(quant_latas, quant_galoes))
print("Preço total: $ {} de galões mais $ {} latas = ${}".format(valor_latas, valor_galoes, valor_total_latas_galoes))
