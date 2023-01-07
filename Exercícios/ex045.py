"""
Exercício 45: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import choice
from time import sleep

opcoesDeEscolha = ["Pedra", "Papel", "Tesoura"]
print("=" * 12)
print("[1] Pedra\n[2] Papel\n[3] Tesoura")
print("=" * 12)
escolhaDoComputador = choice(opcoesDeEscolha)
escolhaDoJogador = int(input("Faça sua jogada: ")) - 1

if escolhaDoJogador >= 0 and escolhaDoJogador <= 2:
	escolhaDoJogador = opcoesDeEscolha[escolhaDoJogador]
	print("\nJO")
	sleep(1)
	print("KEN")
	sleep(1)
	print("PÔ!!!")

	print("=" * 36)
	print("Jogador escolheu {}.\nComputador escolheu {}.".format(escolhaDoJogador, escolhaDoComputador))
	print("=" * 36)
	if escolhaDoJogador == escolhaDoComputador:
		print("EMPATE")
	else:
		if escolhaDoJogador == "Pedra":
			print("Jogador Venceu!" if escolhaDoComputador == "Tesoura" else "Computador Venceu!")
		elif escolhaDoJogador == "Papel":
			print("Jogador Venceu!" if escolhaDoComputador == "Pedra" else "Computador Venceu!")
		elif escolhaDoJogador == "Tesoura":
			print("Jogador Venceu!" if escolhaDoComputador == "Papel" else "Computador Venceu!")
else:
	print("Opção Inválida!")
