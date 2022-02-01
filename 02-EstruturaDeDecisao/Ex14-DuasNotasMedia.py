""" 
   Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de 
   um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo

   O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e 
   a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

    @author Arthur
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
aprovacao = ""
conceito = ""

if media >= 9 and media <= 10:
   aprovacao = "Aprovado"
   conceito = "A"
elif media < 9 and media >= 7.5:
   aprovacao = "Aprovado"
   conceito = "B"
elif media < 7.5 and media >= 6:
   aprovacao = "Aprovado"
   conceito = "C"
elif media < 6 and media >= 4:
   aprovacao = "Reprovado"
   conceito = "D"
elif media < 4 and media >= 0:
   aprovacao = "Reprovado"
   conceito = "E"

print("Nota 1 {} e Nota 2 {} tem média {}".format(nota1, nota2, media))
print("Aluno {} com conceito {}".format(aprovacao, conceito))
