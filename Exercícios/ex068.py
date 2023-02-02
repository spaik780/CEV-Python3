"""
Exercício 68: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print("*" * 30)
print("{:^30}".format("PAR OU ÍMPAR"))
print("*" * 30)

vitoriasConsecutivas = 0

while True:
	valorDoComputador = randint(0,10)
	valorDoJogador = int(input("Diga um valor: "))
	while True:
		jogadorPar = str(input(f"Par ou Ímpar? {valorDoComputador}[P/I] ")).strip().upper()[0]
		if jogadorPar in "PI":
			jogadorPar = jogadorPar == "P"
			break

	valorTotal = valorDoJogador + valorDoComputador
	valorPar = valorTotal % 2 == 0

	print("-" * 60)
	print(f"Você jogou {valorDoJogador} e o computador {valorDoComputador}. Total de {valorTotal}:", end=" ")
	print("PAR" if valorPar else "ÍMPAR")
	print("-" * 60)

	if (jogadorPar and valorPar) or (not jogadorPar and not valorPar):
		print("Você VENCEU!\n")
		print("Vamos jogar novamente...")
		vitoriasConsecutivas += 1
	else:
		break
print("Você PERDEU!\n")
if vitoriasConsecutivas > 0:
	print(f"GAME OVER! Você venceu {vitoriasConsecutivas} vez{'es' if vitoriasConsecutivas > 1 else ''}.")
else:
	print("GAME OVER! Você perdeu de primeira!")
