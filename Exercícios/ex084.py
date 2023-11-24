"""
Exercício 84: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
"""

pessoas = []
dadosDaPessoa = []
menorPeso = maiorPeso = None
while True:
	nomeDaPessoa = str(input("Nome: ")).strip().title()
	pesoDaPessoa = float(input("Peso: "))

	if maiorPeso == None or pesoDaPessoa > maiorPeso:
		maiorPeso = pesoDaPessoa
	if menorPeso == None or pesoDaPessoa < menorPeso:
		menorPeso = pesoDaPessoa

	dadosDaPessoa.append(nomeDaPessoa)
	dadosDaPessoa.append(pesoDaPessoa)
	pessoas.append(dadosDaPessoa[:])
	dadosDaPessoa.clear()

	querContinuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
	if querContinuar == "N": break
print("-" * 50)
print(f"Ao todo você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maiorPeso}Kg. Peso de", end=" ")
for nomeDaPessoa, pesoDaPessoa in pessoas:
	if pesoDaPessoa == maiorPeso:
		print(f"[{nomeDaPessoa}]", end=" ")
print(f"\nO menor peso foi de {menorPeso}Kg. Peso de", end=" ")
for nomeDaPessoa, pesoDaPessoa in pessoas:
	if pesoDaPessoa == menorPeso:
		print(f"[{nomeDaPessoa}]", end=" ")
