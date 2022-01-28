""" 
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
    diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
    regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
    João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
    Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
    que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

    @author Arthur
"""

peso = float(input("Digite quantos quilos de peixe: "))

excesso = peso - 50

multa = excesso * 4

print("São {} kg de peixe".format(peso))
print("O limite de 50kg foi ultrapassado em {} kg de peixe".format(excesso))
print("A multa que deve ser paga é {} $".format(multa))
