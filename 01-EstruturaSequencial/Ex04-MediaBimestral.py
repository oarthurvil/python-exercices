""" 
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    @author Arthur
"""

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

soma = int(nota1) + int(nota2) + int(nota3) + int(nota4)
media = soma / 4

print("A soma das notas é {} e a média é {}".format(soma, media))
