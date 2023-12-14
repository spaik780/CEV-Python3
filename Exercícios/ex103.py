"""
Exercício 103: Ficha do Jogador
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nomeDoJogador="<desconhecido>", quantidadeDeGols="0"):
	return f"O jogador {nomeDoJogador} fez {quantidadeDeGols} gol(s) no campeonato."


nome = str(input("Nome do Jogador: ")).strip().title()
gols = str(input("Quantidade de Gols: ")).strip()

if nome.isalpha() and gols.isnumeric():
	print(ficha(nome, gols))
elif not nome.isalpha() and gols.isnumeric():
	print(ficha(quantidadeDeGols=gols))
elif nome.isalpha() and not gols.isnumeric():
	print(ficha(nomeDoJogador=nome))
else:
	print(ficha())
