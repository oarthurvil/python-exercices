""" 
    A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
    Faça um programa que gere a série até que o valor seja maior que 500.

    @author Arthur
"""

anterior = 0
proximo = 0

while(proximo < 700):
    print(proximo)
    
    proximo = proximo + anterior
    anterior = proximo - anterior

    if(proximo == 0):
        proximo = proximo + 1