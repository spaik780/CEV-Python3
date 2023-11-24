"""
Exercício 88: Palpites Para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from time import sleep
from random import randint

listaDeJogosGerados = []
jogoGerado = []

print("-" * 50)
print("{:^50}".format("JOGA NA MEGA SENA"))
print("-" * 50)
quantidadeDeJogos = int(input("Quantos jogos devem ser sorteados? "))
print("\n{:=^40}".format(f" SORTEANDO {quantidadeDeJogos} JOGOS "))
for contador in range(quantidadeDeJogos):
	sleep(1)
	for _ in range(6):
		while True:
			palpite = randint(1, 60)
			if palpite not in jogoGerado: break
		jogoGerado.append(palpite)
	listaDeJogosGerados.append(sorted(jogoGerado[:]))
	jogoGerado.clear()
	print(f"Jogo {contador + 1}: {listaDeJogosGerados[contador]}")
print("{:=^40}".format(" <BOA SORTE!> "))
