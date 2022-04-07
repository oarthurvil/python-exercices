""" 
    Faça um programa que, dado um conjunto de N números, determine o menor valor, 
    o maior valor e a soma dos valores.

    @author Arthur
"""

quant_num = int(input('Digite a quantidade de números: '))

lista = []
soma = 0

for i in range(0, quant_num):
    num = int(input('Digite o {}º número: '.format(i + 1)))
    lista.append(num)
    soma += num

maior = lista.copy()
maior.sort(reverse=True)

menor = lista.copy()
menor.sort(reverse=False)

print('Soma dos números = {}'.format(soma))
print('Maior dos números = {}'.format(maior[0]))
print('Menor dos números = {}'.format(menor[0]))



