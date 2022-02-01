""" 
    Faça um programa para a leitura de duas notas parciais de um aluno. 
    O programa deve calcular a média alcançada por aluno e apresentar:

        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.

    @author Arthur
"""

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Nota final {} Aprovado com distinção".format(media))
elif media >= 7:
    print("Nota final {} Aprovado".format(media))
elif media < 7:
    print("Nota final {} Reprovado".format(media))