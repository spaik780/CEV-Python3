"""
Exercício 65: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

media = 0
somatoria = 0
querContinuar = True
quantidadeDeNumeros = 0
while querContinuar:
	numero = int(input("Digite um número: "))
	quantidadeDeNumeros += 1
	somatoria += numero
	if quantidadeDeNumeros == 1:
		maiorNumero = numero
		menorNumero = numero
	else:
		if numero > maiorNumero:
			maiorNumero = numero
		elif numero < menorNumero:
			menorNumero = numero
	querContinuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0] == "S"
media = somatoria / quantidadeDeNumeros
print("\nVocê digitou {} números e a média foi {}.".format(quantidadeDeNumeros, media))
print("O maior valor foi {} e o menor foi {}.".format(maiorNumero, menorNumero))
