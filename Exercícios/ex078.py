"""
Exercício 78: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []
for posicao in range(0, 5):
	valores.append(int(input(f"Digite um valor para a posição {posicao}: ")))
print("-" * 50)

maiorValor = max(valores)
menorValor = min(valores)

print(f"Você digitou os valores {valores}")

indice = -1
print(f"O maior valor digitado foi {maiorValor} ", end="nas posições " if valores.count(maiorValor) > 1 else "na posição ")
for _ in range(valores.count(maiorValor)):
	indice = valores.index(maiorValor, indice+1)
	print(indice, end="... ")

indice = -1
print(f"\nO menor valor digitado foi {menorValor} ", end="nas posições " if valores.count(menorValor) > 1 else "na posição ")
for _ in range(valores.count(menorValor)):
	indice = valores.index(menorValor, indice+1)
	print(indice, end="... ")
print()
