""" 
    Supondo que a população de um país A seja da ordem de 80000 habitantes 
    com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
    com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva 
    o número de anos necessários para que a população do país A ultrapasse ou iguale 
    a população do país B, mantidas as taxas de crescimento.
        
    @author Arthur
"""

pais_A = 80000
pais_B = 200000

anos = 0


while pais_A < pais_B:    
    pais_A += pais_A * 0.03
    pais_B += pais_B * 0.015
    anos += 1

print('É necessário {} anos para aproximar o número populacional'. format(anos))