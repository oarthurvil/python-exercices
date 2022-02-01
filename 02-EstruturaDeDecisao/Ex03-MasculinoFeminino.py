""" 
    Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

    @author Arthur
"""

sexo = input("Digite um sexo (M) masculino (F) feminino: ")

if sexo.upper() == "M":
    print("O sexo masculino")
elif sexo.upper() == "F":
    print("O sexo feminino")
else:
    print("O sexo inserido é inválido")