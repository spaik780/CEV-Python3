"""
Exercício 92: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime

trabalhador = {}
trabalhador["nome"] = str(input("Nome: ")).strip().title()
trabalhador["idade"] = datetime.now().year - int(input("Ano de nascimento: "))
trabalhador["ctps"] = int(input("Carteira de trabalho (0 não tem): "))

if trabalhador["ctps"] != 0:
	trabalhador["contratação"] = int(input("Ano de contratação: "))
	trabalhador["salário"] = float(input("Salário: R$"))
	trabalhador["aposentadoria"] = (trabalhador["contratação"] + 35) - (datetime.now().year - trabalhador["idade"])

print("-" * 50)
for chave, valor in trabalhador.items():
	print(f"\t- {chave.upper()} possui o valor {valor}")
