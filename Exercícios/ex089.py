"""
Exercício 89: Boletim com Listas Compostas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

bancoDeDados = []
dadosDoAluno = []
while True:
	nomeDoAluno = str(input("Nome do aluno: ")).strip().title()
	primeiraNotaDoAluno = float(input("1ª Nota: "))
	segundaNotaDoAluno = float(input("2ª Nota: "))
	mediaDoAluno = (primeiraNotaDoAluno + segundaNotaDoAluno) / 2

	dadosDoAluno = [nomeDoAluno, primeiraNotaDoAluno, segundaNotaDoAluno, mediaDoAluno]
	bancoDeDados.append(dadosDoAluno[:])
	dadosDoAluno.clear()

	querContinuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
	if querContinuar == "N": break

print()
print("=" * 30)
print("| {:<8}{:<10}{:>8} |".format("ID.", "Nome", "Média"))
print("|" + "-" * 28 + "|")
for indice in range(len(bancoDeDados)):
	nomeDoAluno = bancoDeDados[indice][0]
	mediaDoAluno = bancoDeDados[indice][3]
	print("| {:<8}{:<10}{:>8} |".format(indice, nomeDoAluno, mediaDoAluno))
print("=" * 30)
print("Digite qualquer outro número para parar.\n")

while True:
	indice = int(input("Mostrar notas de qual aluno? "))
	if 0 <= indice < len(bancoDeDados):
		nomeDoAluno = bancoDeDados[indice][0]
		notasDoAluno = bancoDeDados[indice][1:3]
		print(f"As notas de {nomeDoAluno} são {notasDoAluno}\n")
	else:
		break
print("Programa Finalizado.")
print("<<< VOLTE SEMPRE! >>>")
