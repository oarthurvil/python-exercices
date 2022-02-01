""" 
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    @author Arthur
"""

vogais = ["A", "E", "I", "O", "U"]

while True:
    letra = input("Digite uma letra: ")

    if letra.upper() in vogais:
        print("A letra é uma vogal")
    else:
        print("A letra é uma consoante")
