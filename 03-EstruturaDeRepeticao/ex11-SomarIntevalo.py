""" 
    Faça um programa que receba dois números inteiros e gere os números inteiros 
    que estão no intervalo compreendido por eles, mostrando a soma dos números.

    @author Arthur
"""
num1 = int(input('Digite o número inicial: '))
num2 = int(input('Digite o número final: '))

soma = 0

for i in range(num1, (num2 + 1)):
    print(i)
    soma += i

print('A soma dos intervalos é {}'.format(soma))
    

