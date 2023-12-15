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


def resumo(valor=0, taxaDeAumento=0, taxaDeReducao=0):
	print("-" * 35)
	print("RESUMO DO VALOR".center(35))
	print("-" * 35)
	print("Preço analisado:{:>19}".format(moeda(valor)))
	print("Dobro do preço:{:>20}".format(dobro(valor, True)))
	print("Metade do preço:{:>19}".format(metade(valor, True)))
	print(f"{taxaDeAumento:}% de aumento:" + "{:>20}".format(aumentar(valor, taxaDeAumento, True)))
	print(f"{taxaDeReducao:}% de redução:" + "{:>20}".format(diminuir(valor, taxaDeReducao, True)))
	print("-" * 35)
