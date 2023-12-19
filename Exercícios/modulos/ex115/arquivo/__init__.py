def arquivoExiste(caminhoDoArquivo):
	try:
		open(caminhoDoArquivo).close()
	except:
		return False
	else:
		return True


def criarArquivo(caminhoDoArquivo):
	try:
		open(caminhoDoArquivo, "x").close()
	except:
		print("Erro na criação do arquivo.")
	else:
		print("Arquivo \"ex115_dados.py\" criado.")


def lerArquivo(caminhoDoArquivo, tamanho=50):
	try:
		dados = open(caminhoDoArquivo, encoding="utf-8").read().splitlines()
		for dado in dados:
			nome, idade = dado.split(";")
			print(nome.ljust(tamanho - 9), idade.rjust(3), "anos")
	except:
		print("Erro na leitura do arquivo.")


def gravar(caminhoDoArquivo, nome="<desconhecido>", idade=0):
	try:
		arquivo = open(caminhoDoArquivo, "a", encoding="utf-8")
		arquivo.write(f"{nome};{idade}")
		print(f"Novo registro de {nome} adicionado.")
		arquivo.close()
	except:
		print("Erro na gravação do arquivo.")
