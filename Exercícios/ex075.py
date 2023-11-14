"""
Exercício 75: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares.
"""

numeros = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

print("Você digitou os valores:", numeros)
print(f"O valor 9 apareceu {numeros.count(9)} vezes.")
if 3 in numeros:
	print(f"O valor 3 apareceu pela primeira vez na {numeros.index(3) + 1}ª posição.")
else:
	print("O valor 3 não foi digitado.")
print("Os valores pares digitados foram", end=" ")
for numero in numeros:
	if numero % 2 == 0:
		print(numero, end=" ")
