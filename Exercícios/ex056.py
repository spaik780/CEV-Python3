"""
Exercício 56: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

mediaDeIdade = 0
nomeDoHomemMaisVelho = ""
idadeDoHomemMaisVelho = 0
mulheresComMenosDeVinteAnos = 0
for c in range(1, 5):
	print("----- {}ª PESSOA -----".format(c))
	nome = str(input("Nome: ")).strip().title()
	idade = int(input("Idade: "))
	genero = str(input("Sexo [M/F]: "))[0].strip()

	mediaDeIdade += idade / 4
	if genero in "Mm":
		if idade > idadeDoHomemMaisVelho:
			idadeDoHomemMaisVelho = idade
			nomeDoHomemMaisVelho = nome
	elif genero in "Ff":
		if idade < 20:
			mulheresComMenosDeVinteAnos += 1
print("\nA média de idade do grupo é de {} anos.".format(mediaDeIdade))
print("O homem mais velho tem {} anos e se chama {}.".format(idadeDoHomemMaisVelho, nomeDoHomemMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheresComMenosDeVinteAnos))
