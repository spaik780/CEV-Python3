"""
Exercício 80: Lista Ordenada sem Repetições
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

valores = []
for _ in range(5):
	valorDoUsuario = int(input("Digite um valor: "))
	if not valores or valorDoUsuario > valores[-1]:
		valores.append(valorDoUsuario)
		print("Adicionado ao final da lista.")
	else:
		for indice, valorDaLista in enumerate(valores):
			if valorDoUsuario < valorDaLista:
				valores.insert(indice, valorDoUsuario)
				print(f"Adicionado na posição {indice}")
				break
print("-" * 50)
print(f"Os valores digitados em ordem foram {valores}")
