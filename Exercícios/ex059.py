"""
Exercício 59: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

primeiroNumero = int(input("Primeiro número: "))
segundoNumero = int(input("Segundo número: "))
acao = 0

while acao != 5:
	print("[1] Somar")
	print("[2] Multiplicar")
	print("[3] Maior")
	print("[4] Novos Números")
	print("[5] Sair do Programa")
	acao = int(input("Qual é a sua opção? "))

	if acao == 1:
		soma = primeiroNumero + segundoNumero
		print("A soma entre {} e {} vale {}.".format(primeiroNumero, segundoNumero, soma))
	elif acao == 2:
		produto = primeiroNumero * segundoNumero
		print("A multiplicação entre {} e {} vale {}.".format(primeiroNumero, segundoNumero, produto))
	elif acao == 3:
		if primeiroNumero != segundoNumero:
			maiorNumero = primeiroNumero if primeiroNumero > segundoNumero else segundoNumero
			print("Entre {} e {}, o maior valor é {}.".format(primeiroNumero, segundoNumero, maiorNumero))
		else:
			print("Os dois número são iguais.")
	elif acao == 4:
		primeiroNumero = int(input("Primeiro número: "))
		segundoNumero = int(input("Segundo número: "))
	else:
		print("Opção inválida!")
	print("-" * 30)
	sleep(1)
print("Fim do programa, volte sempre!")
