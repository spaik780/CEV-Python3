"""
Exercício 97: Print Especial
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def escreva(texto):
	tamanho = len(texto) + 2
	print("~" * tamanho)
	print(f"{texto:^{tamanho}}")
	print("~" * tamanho)


escreva("Gustavo Guanabara")
escreva("Curso de Python no Youtube")
escreva("CeV")
