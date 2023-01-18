"""
Exercício 58: Jogo da Adivinhação v2.0
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint

numeroDoComputador = randint(0, 10)
print("[Computador] Acabei de pensar em um número entre 0 e 10.")
print("[Computador] Será que você consegue adivinhar qual foi?\n")

usuarioAcertou = False
tentativas = 0
while not usuarioAcertou:
	numeroDoUsuario = int(input("Qual seu palpite? "))
	tentativas += 1
	if numeroDoUsuario == numeroDoComputador:
		usuarioAcertou = True
	else:
		if numeroDoUsuario > numeroDoComputador:
			print("Menos... Tente novamente!")
		elif numeroDoUsuario < numeroDoComputador:
			print("Mais... Tente novamente!")
print("\nVocê acertou com {} tentativa{}. Parabéns!".format(tentativas, "s" if tentativas > 1 else ""))
