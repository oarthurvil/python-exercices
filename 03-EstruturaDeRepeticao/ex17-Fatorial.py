""" 
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
    Ex.: 5!=5.4.3.2.1=120

    @author Arthur
"""

num = int(input('Digite o número para o fatorial: '))

total = 1
saida = ""

for i in range((num), 0, -1):
    total *= i
    if(i > 1):
        saida += str(i) + "."
    else:
        saida += str(i)
        
print('{}!={} = {}'.format(num, saida, total))
