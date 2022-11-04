"""
Exercício 28: Jogo da Adivinhação v1.0
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

print("Vou pensar em um número entre 0 e 5, tente adivinha-lo!")
sleep(1)
numero = randint(0, 5)
tentativa = int(input("Qual número eu pensei? "))
if (tentativa == numero):
	print("Você acertou! PARABÉNS!")
else:
	print("Você errou! Eu havia pensado no número", numero)
