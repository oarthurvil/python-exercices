""" 
    Informe a população de um país A bem como uma taxa anual de crescimento,
    Informe a população de um país B bem como uma taxa anual de crescimento,
    Faça um programa que calcule e escreva o número de anos necessários para que 
    a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
        
    @author Arthur
"""

pais_A = float(input('Digite a população do país A: '))
pais_B = float(input('Digite a população do país B: '))

cresc_paisA = float(input('Digite a porcentagem de crescimento do país A: '))
cresc_paisB = float(input('Digite a porcentagem de crescimento do país B: '))

anos = 0

while pais_A < pais_B:    
    pais_A += pais_A * (cresc_paisA / 100)
    pais_B += pais_B * (cresc_paisB / 100)
    anos += 1

print('É necessário {} anos para aproximar o número populacional'. format(anos))