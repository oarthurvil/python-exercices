""" 
   Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

    @author Arthur
"""

kilos_morango = float(input("Digite quantos quilos de morango: "))
kilos_maca = float(input("Digite quantos quilos de maçã: "))

preco_morango = 2.50
preco_maca = 1.80


if kilos_morango > 5:
   preco_morango = 2.20

if kilos_maca > 5: 
   preco_maca = 1.50


kilos_totais = kilos_morango + kilos_maca
valor_total = (kilos_morango * preco_morango) + (kilos_maca * preco_maca)

if kilos_totais > 8 or valor_total > 25:
   valor_total -= (valor_total * 0.10)

print("{}Kg morango {}Kg maçã são $ {}".format(kilos_morango, kilos_maca, valor_total)) 