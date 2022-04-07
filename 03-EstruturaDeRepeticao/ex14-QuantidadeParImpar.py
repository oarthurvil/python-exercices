""" 
    Faça um programa que peça 10 números inteiros, 
    calcule e mostre a quantidade de números pares e a quantidade de números impares.

    @author Arthur
"""

numeros = []
pares = 0
impares = 0

for i in range(1, 11):
    num = int(input('Digite {}º número: '.format(i)))
    numeros.append(num)

for numero in numeros:
    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1

print('Os Números são: \nPares {} \nÍmpares {}'.format(pares, impares))