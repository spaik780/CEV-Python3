"""
Exercício 82: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

valores = []
while True:
	valores.append(int(input("Digite um valor: ")))
	querContinuar = str(input("Deseja continuar? [S/N] "))[0].upper()
	if querContinuar == "N": break
valoresPares = []
valoresImpares = []
for valor in valores:
	if valor % 2 == 0:
		valoresPares.append(valor)
	else:
		valoresImpares.append(valor)
print("-" * 50)
print(f"A lista completa é", valores)
print(f"A lista de pares é", valoresPares)
print(f"A lista de ímpares é", valoresImpares)
