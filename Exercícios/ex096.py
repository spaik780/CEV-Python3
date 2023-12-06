"""
Exercício 96: Função Calculadora de Área
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def mostrarTitulo(titulo, tamanho):
	print("-" * tamanho)
	print(f"{titulo:^{tamanho}}")
	print("-" * tamanho)


def área(largura, comprimento):
	area = largura * comprimento
	print(f"A área de um terreno ({largura:.1f} x {comprimento:.1f}) é de {area:.1f}m².")


mostrarTitulo("Controle de Terrenos", 30)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
área(largura, comprimento)
