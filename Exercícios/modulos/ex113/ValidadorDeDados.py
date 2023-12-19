def leiaInt(mensagem):
	while True:
		try:
			numero = int(input(mensagem))
		except ValueError:
			print("\033[31mPor favor, digite um número inteiro válido.\033[m")
			continue
		except KeyboardInterrupt:
			print("\n\033[31mO usuário preferiu não digitar esse número.\033[m")
			return 0
		else:
			return numero


def leiaFloat(mensagem):
	while True:
		try:
			numero = float(input(mensagem))
		except ValueError:
			print("\033[31mPor favor, digite um número real válido.\033[m")
			continue
		except KeyboardInterrupt:
			print("\n\033[31mO usuário preferiu não digitar esse número.\033[m")
			return 0
		else:
			return numero
