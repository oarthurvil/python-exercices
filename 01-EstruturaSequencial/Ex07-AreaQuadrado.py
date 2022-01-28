""" 
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

    @author Arthur
"""

base = input("Digite a base do quadrado: ")
altura = input("Digite a altura do quadrado: ")

area = int(base) * int(altura)
area_dobro = area * 2

print("A área do quadrado é {} e o dobro dela é {}".format(area, area_dobro))