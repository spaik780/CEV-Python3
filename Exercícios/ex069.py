"""
Exercício 69: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""

maioresDeDezoito = 0
quantidadeDeHomens = 0
mulheresComMenosDeVinte = 0

while True:
	print("-" * 30)
	print("{:^30}".format("CADASTRE UMA PESSOA"))
	print("-" * 30)

	idade = int(input("Idade: "))
	while True:
		sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
		if sexo in "MF": break

	if idade > 18: maioresDeDezoito += 1
	if sexo == "M": quantidadeDeHomens += 1
	elif sexo == "F" and idade < 20: mulheresComMenosDeVinte += 1

	while True:
		querContinuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
		if querContinuar in "SN": break
	if querContinuar == "N": break

print(f"\nTotal de pessoas com mais de 18 anos: {maioresDeDezoito}")
if quantidadeDeHomens > 0:
	print(f"Ao todo temos {quantidadeDeHomens} {'homens cadastrados' if quantidadeDeHomens > 1 else 'homem cadastrado'}.")
else:
	print("Nenhum homem foi cadastrado.")
if mulheresComMenosDeVinte > 0:
	print(f"Temos {mulheresComMenosDeVinte} mulher{'es' if mulheresComMenosDeVinte > 1 else ''} com menos de 20 anos.")
else:
	print("Nenhuma mulher com menos de 20 anos foi cadastrada.")
