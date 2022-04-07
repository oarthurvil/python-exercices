""" 
    Faça um programa que leia e valide as seguintes informações:

        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';
        
    @author Arthur
"""

verificar_nome = True
verificar_idade = True
verificar_salario = True
verificar_sexo = True
verificar_estado_civil = True

while(verificar_nome):
    nome = input('Digite o seu nome: ')
    
    if len(nome) > 3:
        verificar_nome = False
    else:
        print('Digite um nome válido')

while(verificar_idade):
    idade = float(input('Digite sua idade: '))

    if idade > 0 and idade < 150:
        verificar_idade = False
    else:
        print('Digite uma idade válida.')
        verificar_idade = False

while(verificar_salario):      
    salario = float(input('Digite seu salário: '))

    if salario > 0:
        verificar_salario = False
    else:
        print('Digite um salário válido')

while (verificar_sexo):  
    sexo = input('Digite o sexo: ').upper()

    if sexo == 'M' or sexo == 'F':
        verificar_sexo = False
    else:
        print('Digite um sexo válido')
        

while(verificar_estado_civil):
    print('Estado civil:')
    print('(S) solteiro')
    print('(C) casado')
    print('(V) viúvo')
    print('(D) divorciado')
    estado_civil = input('Digite o estado civil: ').upper()

    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        verificar_estado_civil = False
    else:
        print('Digite um estado civil válido.')
    
