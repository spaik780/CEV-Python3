"""
Exercício 67: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
	numero = int(input("Quer ver a tabuada de qual valor? "))
	print("-" * 40)
	if numero < 0:
		break
	for c in range(1, 11):
		print(f"{numero} x {c:2} = {numero * c}")
	print("-" * 40)
print("Programa encerrado. Volte sempre!")
