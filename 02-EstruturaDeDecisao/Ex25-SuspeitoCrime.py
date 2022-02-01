""" 
   Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

   "Telefonou para a vítima?"
   "Esteve no local do crime?"
   "Mora perto da vítima?"
   "Devia para a vítima?"
   "Já trabalhou com a vítima?" 

   O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
   entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

    @author Arthur
"""

pergunta_1 = input("Telefonou para a vítima? (S) Sim / (N) Não : ").upper()
pergunta_2 = input("Esteve no local do crime? (S) Sim / (N) Não : ").upper()
pergunta_3 = input("Mora perto da vítima? (S) Sim / (N) Não : ").upper()
pergunta_4 = input("Devia para a vítima? (S) Sim / (N) Não : ").upper()
pergunta_5 = input("Já trabalhou com a vítima? (S) Sim / (N) Não : ").upper()

somador_suspeita = 0

if pergunta_1 == "S":
   somador_suspeita += 1
elif pergunta_1 == "N":
   somador_suspeita += 0
else:
   print("Resposta inválida")
   exit()

if pergunta_2 == "S":
   somador_suspeita += 1
elif pergunta_2 == "N":
   somador_suspeita += 0
else:
   print("Resposta inválida")
   exit()

if pergunta_3 == "S":
   somador_suspeita += 1
elif pergunta_3 == "N":
   somador_suspeita += 0
else:
   print("Resposta inválida")
   exit()

if pergunta_4 == "S":
   somador_suspeita += 1
elif pergunta_4 == "N":
   somador_suspeita += 0
else:
   print("Resposta inválida")
   exit()

if pergunta_5 == "S":
   somador_suspeita += 1
elif pergunta_5 == "N":
   somador_suspeita += 0
else:
   print("Resposta inválida")
   exit()


if somador_suspeita == 2:
   print("Pessoa suspeita.")
elif somador_suspeita == 3 or somador_suspeita == 4:
   print("Pessoa cúmplice.")
elif somador_suspeita == 5:
   print("Pessoa assasina.")
else:
   print("Pessoa inocente.")

