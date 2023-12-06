"""
Exercício 99: Função Para Descobrir o Maior
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(* numeros):
	print("-" * 50)
	print("Analisando os valores passados...")
	maiorValor = 0 if not numeros else numeros[0]
	for numero in numeros:
		print(numero, end=" ")
		if numero > maiorValor:
			maiorValor = numero
	print(f"Foram informados {len(numeros)} valores ao todo.")
	print(f"O maior valor informado foi {maiorValor}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
