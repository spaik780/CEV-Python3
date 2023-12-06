"""
Exercício 100: Funções Para Sortear e Somar
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint

def sorteia(lista):
	print("Sorteando 5 valores da lista:", end=" ")
	for _ in range(5):
		numeroAleatorio = randint(1, 9)
		lista.append(numeroAleatorio)
		print(numeroAleatorio, end=" ")
	print("PRONTO!")


def somaPar(lista):
	soma = 0
	for numero in lista:
		if numero % 2 == 0:
			soma += numero
	print(f"A soma dos valores pares de {lista} vale {soma}.")


numeros = []
sorteia(numeros)
somaPar(numeros)
