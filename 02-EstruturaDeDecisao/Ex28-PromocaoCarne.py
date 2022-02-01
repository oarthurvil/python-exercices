""" 
   UO Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

   Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
   porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
   o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça 
   o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações 
   da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

    @author Arthur
"""

tipo_carne = input("Escolha a carne:\n(F) Filé Duplo\n(A) Alcatra\n(P) Picanha\n").upper()
quant_carne = float(input("Digite quantos quilos de carne: "))

preco_carne = 0

if tipo_carne == "F":
   if quant_carne < 5:
      preco_carne = 4.90
   else:
      preco_carne = 5.80
elif tipo_carne == "A":
   if quant_carne < 5:
      preco_carne = 5.90
   else:
      preco_carne = 6.80
elif tipo_carne == "P": 
   if quant_carne < 5:
      preco_carne = 6.90
   else:
      preco_carne = 7.80
else:
   print("Digite um tipo de carne válido.")
   exit()

cartao = input("Deseja pagar com cartão Tabajara? (S) sim / (N) não: ").upper()

total = quant_carne * preco_carne
desconto = 0

if cartao == "S":
   desconto = total * 0.05
   total -= desconto
elif cartao == "N":
   desconto = 0
else:
   print("Digite uma opção válida.")
   exit()

print(" Tipo de carne {}".format(tipo_carne))
print(" Quantidade de carne {}".format(quant_carne))
print(" Cartão Tabajara {}".format(cartao))
print(" Valor Desconto $ {}".format(round(desconto, 2)))
print(" Preço total $ {}".format(total))