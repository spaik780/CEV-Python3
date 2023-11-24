"""
Exercício 83: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

parenteses = []
expressaoValida = True
expressao = str(input("Digite a expressão: "))

for caractere in expressao:
	if caractere in "()":
		parenteses.append(caractere)

if parenteses.count("(") != parenteses.count(")"):
	expressaoValida = False
else:
	for indice in range(int(len(parenteses) / 2)):
		indiceDoParenteseAberto = parenteses.index("(")
		indiceDoParenteseFechado = parenteses.index(")")
		if indiceDoParenteseAberto > indiceDoParenteseFechado:
			expressaoValida = False
			break
		else:
			parenteses.remove("(")
			parenteses.remove(")")
print("Sua expressão está", "válida!" if expressaoValida else "inválida!")
