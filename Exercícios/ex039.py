"""
Exercício 39: Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

import datetime

anoAtual = datetime.date.today().year
anoDeNascimento = int(input("Informe o ano de nascimento: "))
idade = anoAtual - anoDeNascimento
if idade == 18:
	print("É hora de se alistar.")
elif idade < 18:
	print("Você vai se alistar daqui {} ano(s)".format(18 - idade))
elif idade > 18:
	print("Você já devia ter se alistado há {} ano(s).".format(idade - 18))
