"""
Exercício 54: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

anoAtual = date.today().year
maioresDeIdade = 0
menoresDeIdade = 0
for c in range(1, 8):
	idade = anoAtual - int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
	if idade > 21:
		maioresDeIdade += 1
	else:
		menoresDeIdade += 1
print()
print("Ao todo tivemos {} pessoas maiores de idade".format(maioresDeIdade))
print("E também tivemos {} pessoas menores de idade".format(menoresDeIdade))
