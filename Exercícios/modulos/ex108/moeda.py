def aumentar(valor=0, taxa=0):
	resultado = valor + valor * taxa / 100
	return resultado


def diminuir(valor=0, taxa=0):
	resultado = valor - valor * taxa / 100
	return resultado


def metade(valor=0):
	resultado = valor / 2
	return resultado


def dobro(valor=0):
	resultado = valor * 2
	return resultado


def moeda(valor=0, cifrao="R$"):
	valorFormatado = "{}{:.2f}".format(cifrao, valor).replace(".", ",")
	return valorFormatado
