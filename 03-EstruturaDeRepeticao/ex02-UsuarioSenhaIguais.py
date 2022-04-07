""" 
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
    senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

    @author Arthur
"""

verificar = True

while(verificar):
    usuario = input("Digite o seu usuário: ").upper()
    senha = input("Digite sua senha: ").upper()

    if usuario == senha:
        print('Usuário e senha não podem ser os mesmos.')
    else:
        print('Usuário e senha aceitos.')
        verificar = False