""" 
   Um posto está vendendo combustíveis com a seguinte tabela de descontos:

      Álcool:
      até 20 litros, desconto de 3% por litro
      acima de 20 litros, desconto de 5% por litro

      Gasolina:
      até 20 litros, desconto de 4% por litro
      Acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
      o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
      a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do 
      álcool é R$ 1,90.

    @author Arthur
"""

litros_combust = float(input("Digite quantos litros de combustível: "))
tipo_combust = input("Digite o tipo de combustível:\n(A) álcool\n(G) gasolina\n").upper()

preco_alcool = 1.90
preco_gasolina = 2.50

desconto = 0
valor_total = 0

if tipo_combust == "A":
   if litros_combust <= 20:
      desconto = preco_alcool * 0.03
      valor_total = litros_combust * (preco_alcool - desconto)
   else:
      desconto = preco_alcool * 0.05
      valor_total = litros_combust * (preco_alcool - desconto)
elif tipo_combust == "G":
   if litros_combust <= 20:
      desconto = preco_alcool * 0.04
      valor_total = litros_combust * (preco_gasolina - desconto)
   else:
      desconto = preco_alcool * 0.06
      valor_total = litros_combust * (preco_gasolina - desconto)
else:
   print("Digite um tipo de combutível válido.")


print("{} litros de {} são = ${}".format(litros_combust, tipo_combust, valor_total))