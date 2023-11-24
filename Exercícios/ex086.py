"""
Exercício 86: Matriz em Python
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for indiceDaLinha in range(3):
	for indiceDaColuna in range(3):
		numero = int(input(f"Digite um valor para [{indiceDaLinha}, {indiceDaColuna}]: "))
		matriz[indiceDaLinha][indiceDaColuna] = numero
print("-" * 50)
for indiceDaLinha in range(3):
	for indiceDaColuna in range(3):
		numero = matriz[indiceDaLinha][indiceDaColuna]
		print(f"[{numero:^5}]", end="")
	print()
