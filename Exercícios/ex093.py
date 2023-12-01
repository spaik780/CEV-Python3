"""
Exercício 93: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

fichaDoJogador = {
	"nome": str(input("Nome do jogador: ")).strip().title(),
	"gols": [],
	"total": 0
}

for indice in range(int(input(f"Quantas partidas {fichaDoJogador['nome']} jogou? "))):
	quantidadeDeGols = int(input(f"\tQuantos gols na {indice + 1}ª partida? "))
	fichaDoJogador["gols"].append(quantidadeDeGols)
fichaDoJogador["total"] = sum(fichaDoJogador["gols"])

print("-" * 60)
print(fichaDoJogador)

print("-" * 60)
for chave, valor in fichaDoJogador.items():
	print(f"O campo {chave.upper()} possui o valor {valor}")

print("-" * 60)
print(f"O jogador {fichaDoJogador['nome']} jogou {len(fichaDoJogador['gols'])} partidas.")
for indice, quantidadeDeGols in enumerate(fichaDoJogador["gols"]):
	print(f"\t=> Na {indice + 1}ª partida fez {quantidadeDeGols} gols.")
print(f"Foi um total de {fichaDoJogador['total']} gols.")
