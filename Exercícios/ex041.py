"""
Exercício 41: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

anoAtual = date.today().year
anoDeNascimento = int(input("Ano de Nascimento: "))
idade = anoAtual - anoDeNascimento
print("O atleata tem {} anos.".format(idade))
print("Classificação:", end=" ")
if idade <= 9:
	print("MIRIM")
elif idade <= 14:
	print("INFANTIL")
elif idade <= 19:
	print("JUNIOR")
elif idade <= 25:
	print("SÊNIOR")
else:
	print("MASTER")
