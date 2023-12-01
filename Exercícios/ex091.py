"""
Exercício 91: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint, choice
from operator import itemgetter
from time import sleep

listaDeNomes = ["Sofia", "Vitor", "Maria", "João", "Paulo", "Bárbara", "Pedro", "Gabriel"]
jogadores = {}

for indice in range(4):
	nomeDoJogador = choice(listaDeNomes)
	dadoDoJogador = randint(1, 6)

	jogadores[nomeDoJogador] = dadoDoJogador
	listaDeNomes.remove(nomeDoJogador)
	print(f"{nomeDoJogador} tirou {dadoDoJogador} no dado.")
	sleep(1)

print("-" * 51)
print("{:^51}".format("===== RANKING DOS JOGADORES ====="))
for indice, (nomeDoJogador, dadoDoJogador) in enumerate(sorted(jogadores.items(), key=itemgetter(1), reverse=True)):
	print("{:^51}".format(f"{indice+1}º Lugar: {nomeDoJogador:7} com {dadoDoJogador}"))
	sleep(1)
