"""
Exercício 105: Analisando e Gerando Dicionários
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas.
- A maior nota.
- A menor nota.
- A média da turma.
- A situação (opcional).
"""

def notas(*notas, showSit=False):
	"""
	Analisa várias notas de alunos.
	:param notas: Uma ou mais notas.
	:param showSit: (Opcional) Adicionar a situação.
	:return: Dicionário com informações sobre a turma.
	"""
	dicionario = {
		"QUANTIDADE DE NOTAS": len(notas),
		"MAIOR": max(notas),
		"MENOR": min(notas),
		"MÉDIA": sum(notas) / len(notas),
	}
	if showSit:
		if dicionario["MÉDIA"] >= 7:
			dicionario["SITUAÇÃO"] = "BOA"
		elif dicionario["MÉDIA"] >= 5:
			dicionario["SITUAÇÃO"] = "RAZOÁVEL"
		else:
			dicionario["SITUAÇÃO"] =  "RUIM"
	return dicionario


help(notas)

print("\nTURMA 01")
print(notas(4, 7, 6, 10, 4.5, 9.5, 10, 10, 0, showSit=True))

print("\nTURMA 02")
print(notas(10, 10, 10, showSit=True))

print("\nTURMA 03")
print(notas(4.5, 7, 2.5, 5, showSit=True))
