def calcularFatorial(numero):
	fatorial = 1
	for indice in range(1, numero + 1):
		fatorial *= indice
	return fatorial


def calcularDobro(numero):
	return numero * 2


def calcularTriplo(numero):
	return numero * 3
