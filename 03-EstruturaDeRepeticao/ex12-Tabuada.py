""" 
    Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
    número inteiro entre 1 a 10. O usuário deve informar de qual numero ele 
    deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    @author Arthur
"""

num = int(input('Digite o número para ver a tabuada: '))

print('Tabuada de {}:'.format(num))

for i in range(1, 11):
    tabuada = num * i    
    print('{} x {} = {}'.format(num, i, tabuada))