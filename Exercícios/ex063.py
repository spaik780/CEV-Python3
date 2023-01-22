"""
Exercício 63: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print("-" * 30)
print("{:^30}".format("Sequência de Fibonacci"))
print("-" * 30)

contador = 0
quantidadeDeTermos = int(input("Quantos termos você quer mostrar? "))
termoAnterior = -1
termoAtual = 0
termoPosterior = 1

while contador < quantidadeDeTermos:
	termoAtual = termoAnterior + termoPosterior
	print(termoAtual, end=" -> ")
	termoAnterior = termoPosterior
	termoPosterior = termoAtual
	contador += 1
print("FIM")
