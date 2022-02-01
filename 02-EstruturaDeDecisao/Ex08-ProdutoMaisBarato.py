""" 
   Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
   sabendo que a decisão é sempre pelo mais barato.

    @author Arthur
"""

produto1 = float(input("Digite o preço do produto: "))
produto2 = float(input("Digite o preço do produto: "))
produto3 = float(input("Digite o preço do produto: "))


if produto1 < produto2 and produto1 < produto3:
    print("O menor entre ${} ${} ${} é ${}".format(produto1, produto2, produto3, produto1))
elif produto2 < produto1 and produto2 < produto3:
    print("O menor entre ${} ${} ${} é ${}".format(produto1, produto2, produto3, produto2))
else:
    print("O menor entre ${} ${} ${} é ${}".format(produto1, produto2, produto3, produto3))