"""
Exercício 61: Progressão Aritmética v2.0
Refaça o Exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiroTermo

while termo < primeiroTermo + 10 * razao:
	print(termo, end=" -> ")
	termo += razao
print("FIM")
