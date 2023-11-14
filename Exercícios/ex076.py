"""
Exercício 76: Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

produtos = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("-" * 50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("-" * 50)

for c in range(0, len(produtos), 2):
	nomeDoProduto = produtos[c]
	valorDoProduto = produtos[c+1]
	print(nomeDoProduto, end = '.' * (50 - len(nomeDoProduto) - 9))
	print(f"R${valorDoProduto:>7.2f}")
print("-" * 50)
