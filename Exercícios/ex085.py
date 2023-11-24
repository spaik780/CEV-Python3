"""
Exercício 85: Listas com Pares e Ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros = [[],[]]
for contador in range(1, 8):
	numero = int(input(f"Digite o {contador}º valor: "))
	numeros[numero % 2].append(numero)
numeros[0].sort()
numeros[1].sort()
print("-" * 50)
print("Os valores pares digitados foram", numeros[0])
print("Os valores ímpares digitados foram", numeros[1])
