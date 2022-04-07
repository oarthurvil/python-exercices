""" 
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
    o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

    @author Arthur
"""

continua_loop = True

while(continua_loop):
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida.")
    else:
        print("Nota válida, nota {}".format(nota))
        continua_loop = False 