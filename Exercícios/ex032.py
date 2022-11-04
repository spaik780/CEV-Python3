"""
Exercício 32: Ano Bissexto
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date

ano = int(input("Informe um ano para ser analisado (0 para o ano atual): "))
ano = date.today().year if ano == 0 else ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print("O ano de {} é BISSEXTO!".format(ano))
else:
	print("O ano de {} NÃO É BISSEXTO!".format(ano))
