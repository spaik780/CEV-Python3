def linha(tamanho=50):
	return "-" * tamanho


def cabecalho(titulo, tamanho=50):
	print(linha(tamanho))
	print(titulo.center(tamanho))
	print(linha(tamanho))


def menu(*opcoes):
	cabecalho("MENU PRINCIPAL")
	for indice, opcao in enumerate(opcoes):
		print(f"\033[33m{indice + 1}\033[30m - \033[34m{opcao}\033[m")
	print(linha())

	return leiaInt("\033[33mSua opção: \033[m")
			

def leiaInt(mensagem):
	while True:
		try:
			numero = int(input(mensagem))
		except:
			print("\033[31mPor favor, digite um número inteiro válido.\033[m")
			continue
		else:
			return numero
