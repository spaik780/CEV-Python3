"""
Exercício 33: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
maior = numero1
menor = numero1

if numero2 > maior or numero3 > maior:
	maior = numero2 if numero2 > numero3 else numero3
if numero2 < menor or numero3 < menor:
	menor = numero2 if numero2 < numero3 else numero3

print("O maior número digitado foi {}.".format(maior))
print("O menor número digitado foi {}.".format(menor))
