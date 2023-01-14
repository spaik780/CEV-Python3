"""
Exercício 51: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for termo in range(primeiroTermo, primeiroTermo + 10 * razao, razao):
	print(termo, end=" > ")
print("ACABOU")
