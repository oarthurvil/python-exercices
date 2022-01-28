""" 
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
    -Para homens: (72.7*h) - 58
    -Para mulheres: (62.1*h) - 44.7

    @author Arthur
"""

altura = float(input("Digite sua altura em metros: "))

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print("Seu peso ideal é: \n Para Homem - {} kg".format(round(peso_ideal_homem, 2)))
print("Seu peso ideal é: \n Para Mulher - {} kg".format(round(peso_ideal_mulher, 2)))