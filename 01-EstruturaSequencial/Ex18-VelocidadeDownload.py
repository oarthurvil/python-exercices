""" 
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
    link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este 
    link (em minutos).

    @arthur
"""

arquivo = int(input("Digite o tamanho do arquivo em MB: "))
velocidade = int(input("Digite a velocidade em MBs: "))

tempo = arquivo / velocidade
tempo_minutos = int(tempo / 60)
tempo_segundos = ((tempo / 60) - tempo_minutos) * 60

print("Tempo de download {} minutos {} segundos".format(tempo_minutos, round(tempo_segundos, 2)))