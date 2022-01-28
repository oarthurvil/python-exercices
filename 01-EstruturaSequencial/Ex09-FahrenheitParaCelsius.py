""" 
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).

    @author Arthur
"""

graus_fahrenheit = float(input("Digite quantos graus Fahrenheit: "))

graus_celsius = 5 * ((graus_fahrenheit - 32) / 9)

print("{} ºF são {} ºC".format(graus_fahrenheit, graus_celsius))