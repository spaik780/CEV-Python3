"""
Exercício 70: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

querContinuar = True
valorTotal = 0
contador = 0
produtosValendoMaisDeMil = 0
nomeDoProdutoMaisBarato = ""
valorDoProdutoMaisBarato = 0

print("-" * 30)
print("{:^30}".format("LOJA SUPER BARATÃO"))
print("-" * 30)

while querContinuar:
	contador += 1
	nomeDoProduto = str(input("Nome do Produto: ")).strip().title()
	valorDoProduto = float(input("Preço: R$"))

	valorTotal += valorDoProduto
	if valorDoProduto > 1000.00: produtosValendoMaisDeMil += 1
	if valorDoProduto < valorDoProdutoMaisBarato or contador == 1:
		nomeDoProdutoMaisBarato = nomeDoProduto
		valorDoProdutoMaisBarato = valorDoProduto

	while True:
		querContinuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
		if querContinuar in "SN": querContinuar = querContinuar == "S"; break

print("{:-^30}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi de R${valorTotal:.2f}")
print(f"Temos {produtosValendoMaisDeMil} produto{'s' if produtosValendoMaisDeMil > 1 else ''} custando mais de R$1000,00")
print(f"O produto mais barato foi {nomeDoProdutoMaisBarato} custando R${valorDoProdutoMaisBarato:.2f}")
