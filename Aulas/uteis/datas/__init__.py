from datetime import datetime


def calcularIdade(anoDeNascimento):
	anoAtual = datetime.now().year
	idade = anoAtual - anoDeNascimento
	return idade
