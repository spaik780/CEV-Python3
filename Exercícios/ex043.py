"""
Exercício 43: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))
imc = peso / altura ** 2

print("Status do IMC ({:.2f}):".format(imc), end=" ")
if imc < 18.5:
	print("Abaixo do Peso")
elif imc < 25:
	print("Peso Ideal")
elif imc < 30:
	print("Sobrepeso")
elif imc < 40:
	print("Obesidade")
else:
	print("Obesidade Mórbida")
