# Função Retornável
def fatorialDoNumero(numero = 1):
	"""
	Calcula e retorna o fatorial de um número.
	:param numero: Número para ser calculado.
	:return: O fatorial.
	"""
	fatorial = 1
	for contador in range(numero, 0, -1):
		fatorial *= contador
	return fatorial


print("O fatorial de 5, 6 e 7 são respectivamente {}, {} e {}".format(
	fatorialDoNumero(5),
	fatorialDoNumero(6),
	fatorialDoNumero(7)
))

# Docstring
def contador(i, f, p=1):
	"""
	Faz uma contagem e mostra na tela.
	:param i: Início da contagem.
	:param f: Fim da contagem.
	:param p: Passo da contagem.
	:return: Sem retorno.
	"""
	c = i
	while c <= f:
		print(c, end=" ")
		c += p
	print("FIM!")


contador(2, 10, 2)

# Escopo de Variáveis
def teste(b):
	global a
	b += 4
	c = 2
	print("[a] dentro vale", a) # 5
	print("[b] dentro vale", b) # 9
	print("[c] dentro vale", c) # 2

	a = 8
	print("[a] dentro vale", a) # 8


a = 5
teste(a)
print("[a] fora vale", a) # 8
# print("[b] fora vale", b) > ERRO
# print("[c] fora vale", c) > ERRO