def mostrarLinha(tamanhoDaLinha):
	print("-" * tamanhoDaLinha)

def somarDoisNumeros(n1, n2):
	print(f"N1 = [{n1}], N2 = [{n2}]", end=" | ")
	print(f"N1 + N2 = [{n1 + n2}]")

def somarNumeros(* numeros):
	somaDosNumeros = 0
	for numero in numeros:
		somaDosNumeros += numero
	print(f"A soma dos números {numeros} vale {somaDosNumeros}.")


# Programa Principal
mostrarLinha(50)
somarDoisNumeros(4, 5) # 9
somarDoisNumeros(8, 9) # 17
somarDoisNumeros(2, 1) # 3
mostrarLinha(50)
somarNumeros(3, 7, 2, 5)
somarNumeros(2, 8, 2)
somarNumeros(2, 2)
mostrarLinha(50)
