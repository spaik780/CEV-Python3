"""
Exercício 52: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

quantidadeDeDivisoes = 0
numero = int(input("Digite um número: "))
for c in range(1, numero + 1):
	if numero % c == 0:
		print("\033[33m{}".format(c), end=" ")
		quantidadeDeDivisoes += 1
	else:
		print("\033[31m{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(numero, quantidadeDeDivisoes))
print("E por isso ele {}".format("É PRIMO!" if quantidadeDeDivisoes == 2 else "NÃO É PRIMO"))
