""" 
    Faça um programa que leia 5 números e informe o maior número.
        
    @author Arthur
"""

lista = []
maior = []

for i in range(1, 6):
    numero = float(input('Digite o {}º número: '.format(i)))
    lista.append(numero)

lista.sort(reverse=True)


print('O maior número informado é {}'.format(lista[0]))


