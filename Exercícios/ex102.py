"""
Exercício 102: Função Para Fatorial
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(numero, show=False):
	"""
	Calcula o fatorial de um número.
	:param numero: O número a ser calculado.
	:param show: (Opcional) Mostra ou não o cálculo.
	:return: Valor do fatorial do número.
	"""
	fatorialDoNumero = 1
	for indice in range(numero, 0, -1):
		fatorialDoNumero *= indice
		if show:
			print(indice, end=" x " if indice > 1 else " = ")
	return fatorialDoNumero


print(fatorial(5))
print(fatorial(5, True))
help(fatorial)
