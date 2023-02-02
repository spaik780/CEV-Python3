"""
Exercício 66: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, sendo a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o Flag).
"""

somatoria = 0
quantidadeDeNumeros = 0
while True:
	numero = int(input("Digite um número (999 para parar): "))
	if numero == 999:
		break
	somatoria += numero
	quantidadeDeNumeros += 1
print(f"Você digitou {quantidadeDeNumeros} números e a soma entre eles vale {somatoria}.")
