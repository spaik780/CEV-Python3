"""
Exercício 12: Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input("Informe o preço de um produto para ser aplicado o desconto: R$"))
print("O valor do produto agora é de R${:.2f}".format(preco - (preco * 0.05)))
