"""
Exercício 94: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
- Quantas pessoas cadastradas.
- A média de idade.
- Uma lista com mulheres.
- Uma lista com idade acima da média.
"""

mediaDeIdade = 0
bancoDeDados = []
while True:
	nome = str(input("Nome: ")).strip().title()
	while True:
		sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
		if sexo in "MF":
			break
		print("Sexo inválido! Digite apenas [M] ou [F].")
	while True:
		idade = str(input("Idade: ")).strip()
		if idade.isnumeric() and int(idade) > 0:
			idade = int(idade)
			break
		print("Idade inválida! Tente novamente.")

	dadosDaPessoa = {
		"NOME": nome,
		"SEXO": sexo,
		"IDADE": idade 
	}
	bancoDeDados.append(dadosDaPessoa.copy())
	dadosDaPessoa.clear()

	mediaDeIdade += (idade - mediaDeIdade) / len(bancoDeDados)

	while True:
		querContinuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
		if querContinuar in "SN":
			break
		print("Resposta inválida! Digite apenas [S] ou [N].")
	if querContinuar == "N": break

print("-" * 50)
print(f"\tAo todo temos {len(bancoDeDados)} pessoas cadastradas.")
print(f"\tA média de idade é de {mediaDeIdade:.2f} anos.")
print("\tAs mulheres cadastradas foram", end=" ")
for dadosDaPessoa in bancoDeDados:
	if dadosDaPessoa["SEXO"] == "F":
		print(f"[{dadosDaPessoa['NOME']}]", end=" ")
print("\n\tLista de Pessoas que estão acima da média: ")
for dadosDaPessoa in bancoDeDados:
	if dadosDaPessoa["IDADE"] >= mediaDeIdade:
		print(end="\t- ")
		for chave, valor in dadosDaPessoa.items():
			print(f"{chave}: {valor};", end=" ")
		print()
print("<<< FIM DO PROGRAMA >>>")
