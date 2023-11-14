"""
Exercício 74: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""

from random import randint

numerosSorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print("Os valores sorteados foram:", end=" ")
for numero in numerosSorteados:
	print(numero, end=" ")
print("\nO maior valor sorteado foi", max(numerosSorteados))
print("O menor valor sorteado foi", min(numerosSorteados))
