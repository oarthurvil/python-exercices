""" 
    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    F = (0°C × 9/5) + 32 

    @author Arthur
"""

graus_celsius = float(input("Digite quantos graus Celsius: "))

graus_fahrenheit = (graus_celsius * (9 / 5)) + 32

print("{} ºC são {} ºF".format(graus_celsius, graus_fahrenheit))