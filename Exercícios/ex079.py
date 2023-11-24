"""
Exercício 79: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

valores = []
while True:
	valor = int(input("Digite um valor: "))
	if valor in valores:
		print(f"O número {valor} já foi adicionado.")
	else:
		valores.append(valor)
		print(f"Número {valor} adicionado!")

	querContinuar = str(input("Deseja continuar? [S/N] "))[0].upper()
	if querContinuar == "N": break
valores.sort()
print("-" * 50)
print(f"Você digitou os valores {valores}")
