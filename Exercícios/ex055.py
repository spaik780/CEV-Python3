"""
Exercício 55: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
	peso = float(input("Peso da {}ª pessoa (Kg): ".format(c)))
	if c == 1:
		maiorPeso = peso
		menorPeso = peso
	else:
		if peso > maiorPeso:
			maiorPeso = peso
		if peso < menorPeso:
			menorPeso = peso
print("O maior peso lido foi de {}Kg".format(maiorPeso))
print("O menor peso lido foi de {}Kg".format(menorPeso))
