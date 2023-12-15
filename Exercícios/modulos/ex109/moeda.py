def aumentar(valor=0, taxa=0, formatar=False):
	resultado = valor + valor * taxa / 100
	return moeda(resultado) if formatar else resultado


def diminuir(valor=0, taxa=0, formatar=False):
	resultado = valor - valor * taxa / 100
	return moeda(resultado) if formatar else resultado


def metade(valor=0, formatar=False):
	resultado = valor / 2
	return moeda(resultado) if formatar else resultado


def dobro(valor=0, formatar=False):
	resultado = valor * 2
	return moeda(resultado) if formatar else resultado


def moeda(valor=0, cifrao="R$"):
	valorFormatado = "{}{:.2f}".format(cifrao, valor).replace(".", ",")
	return valorFormatado
