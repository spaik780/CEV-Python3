"""
Exercício 90: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}
aluno["nome"] = str(input("Nome: ")).strip().title()
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["média"] < 5:
	aluno["situação"] = "Reprovado"
elif aluno["média"] < 7:
	aluno["situação"] = "Recuperação"
else:
	aluno["situação"] = "Aprovado"

print("-" * 50)
for chave, valor in aluno.items():
	print(f"> {chave.upper()} é igual a {valor}.")
print("-" * 50)
