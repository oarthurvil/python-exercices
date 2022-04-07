""" 
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
    Permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números 
    inteiros positivos e menores que 16.

    OBS: Aceite apenas números entre 0 e 1000.

    @author Arthur
"""

while(True):
    num = int(input('Digite o número para o fatorial, inteiros, positivo e menores que 16: '))

    total = 1
    saida = ""
    
    if(num > 0 and num < 16):
        for i in range((num), 0, -1):
            total *= i
            if(i > 1):
                saida += str(i) + "."
            else:
                saida += str(i)
                
        print('{}!={} = {}'.format(num, saida, total))
    else:
        print('Fatorial inválido')


