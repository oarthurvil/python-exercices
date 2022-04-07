""" 
    Faça um programa que leia 5 números e informe a soma e a média dos números.

    @author Arthur
"""

lista = []
soma = 0

for i in range(1, 6):
    numero = float(input('Digite o {}º número: '.format(i)))
    lista.append(numero)
    soma += lista[i-1]

media = soma / 5

print('A soma é {}'.format(soma))
print('A média é {}'.format(media))


