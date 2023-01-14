"""
Exercício 50: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

somatoriaDosPares = 0
quantidadeDePares = 0
for c in range(1, 7):
	numero = int(input("Digite o {}º valor: ".format(c)))
	if numero % 2 == 0:
		quantidadeDePares += 1
		somatoriaDosPares += numero
print("Você informou {} números PARES e a soma foi {}.".format(quantidadeDePares, somatoriaDosPares))
