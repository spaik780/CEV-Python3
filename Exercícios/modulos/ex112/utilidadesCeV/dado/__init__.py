def leiaDinheiro(mensagem):
	while True:
		valor = str(input(mensagem))
		valorValidado = valor.strip().replace(",", ".")
		if valorValidado.replace(".", "").isnumeric() and valorValidado.count(".") <= 1:
			return float(valorValidado)
		else:
			print(f"\033[31mERRO: \"{valor}\" é um preço inválido!\033[m")
