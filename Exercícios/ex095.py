"""
Exercício 95: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

bancoDeDados = []
while True:
	dadosDoJogador = {
		"NOME": "",
		"GOLS": [],
		"TOTAL": 0
	}

	dadosDoJogador["NOME"] = str(input("Nome do jogador: ")).strip().title()
	for indice in range(int(input(f"Quantas partidas {dadosDoJogador['NOME']} jogou? "))):
		quantidadeDeGols = int(input(f"\tQuantos gols na {indice + 1}ª partida? "))
		dadosDoJogador["GOLS"].append(quantidadeDeGols)
	dadosDoJogador["TOTAL"] = sum(dadosDoJogador["GOLS"])

	bancoDeDados.append(dadosDoJogador.copy())
	del(dadosDoJogador)

	while True:
		querContinuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
		if querContinuar in "SN":
			break
		print("Resposta inválida! Digite apenas [S] ou [N].")
	if querContinuar == "N": break

print()
print("=" * 46)
print("| {:<6}{:<12}{:<18}{:>6} |".format("COD", "NOME", "GOLS", "TOTAL"))
print("|" + "-" * 44 + "|")
for indice, dadosDoJogador in enumerate(bancoDeDados):
	print("| {:<6}{:<12}{:<18}{:>6} |".format(
		indice,
		dadosDoJogador["NOME"],
		str(dadosDoJogador["GOLS"]),
		dadosDoJogador["TOTAL"])
	)
print("=" * 46)
print("Digite 999 para parar.")

while True:
	indice = int(input("\nMostrar dados de qual jogador? "))
	if 0 <= indice < len(bancoDeDados):
		print(f"Levantamento do jogador [{bancoDeDados[indice]['NOME']}]:")
		for indice, quantidadeDeGols in enumerate(bancoDeDados[indice]["GOLS"]):
			print(f"- No {indice + 1}º jogo fez {quantidadeDeGols} gols.")
	elif indice == 999:
		break
	else:
		print(f"Não existe jogador com código {indice}!")
print("Programa Finalizado.")
print("<<< VOLTE SEMPRE! >>>")
