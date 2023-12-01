from operator import itemgetter

jogadores = { # Nome e Pontuação
	"João": 9,
	"Paulo": 5,
	"Maria": 7,
	"Sofia": 10
}

ranking1 = sorted(jogadores, key=jogadores.get, reverse=True)
ranking2 = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking1) # ["Sofia", "João", "Maria", "Paulo"]
print(ranking2) # [("Sofia", 10), ("João", 9), ("Maria", 7), ("Paulo", 5)]

estado = {}
brasil = []

estado["uf"] = "Rio de Janeiro"
estado["sigla"] = "RJ"
brasil.append(estado.copy())

estado["uf"] = "São Paulo"
estado["sigla"] = "SP"
brasil.append(estado.copy())

estado["uf"] = "Goiás"
estado["sigla"] = "GO"
brasil.append(estado.copy())

del(estado)
for estado in brasil:
	print(type(estado), estado)
	print(f"A unidade federativa {estado['uf'].title()} possui a sigla {estado['sigla'].upper()}.")
	for chave, valor in estado.items(): # estado.keys(), estado.values()
		print(f"o campo [{chave}] tem o valor [{valor}]")
	print()
