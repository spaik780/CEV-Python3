"""
Exercício 87: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
- A soma de todos os valores pares digitados.
- A soma dos valores da terceira coluna.
- O maior valor da segunda linha.
"""

somaDosPares = somaDaTerceiraColuna = 0
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for indiceDaLinha in range(3):
	for indiceDaColuna in range(3):
		numero = int(input(f"Digite um valor para [{indiceDaLinha}, {indiceDaColuna}]: "))
		matriz[indiceDaLinha][indiceDaColuna] = numero

		if numero % 2 == 0:
			somaDosPares += numero
		if indiceDaColuna == 2:
			somaDaTerceiraColuna += numero
print("-" * 50)
for indiceDaLinha in range(3):
	for indiceDaColuna in range(3):
		numero = matriz[indiceDaLinha][indiceDaColuna]
		print(f"[{numero:^5}]", end="")
	print()
print("-" * 50)
print("A soma dos valores pares vale", somaDosPares)
print("A soma dos valores da terceira coluna vale", somaDaTerceiraColuna)
print("O maior valor da segunda linha é", max(matriz[1]))
