""" 
   Faça um Programa que pergunte em que turno você estuda. 
   Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
   Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    @author Arthur
"""

turno = input("Digite o turno \n (M) Matutino \n (V) Vespertino \n (N) Noturno \n")

turno_uppercase = turno.upper()

if turno_uppercase == "M":
   print("Bom Dia!")
elif turno_uppercase == "V":
   print("Boa Tarde!")
elif turno_uppercase == "N":
   print("Boa Noite!")
else:
   print("Valor inválido!")