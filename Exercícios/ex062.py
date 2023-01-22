"""
Exercício 62: Super Progressão Aritmética v3.0
Melhore o Exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiroTermo
termosParaMostrar = 10
quantidadeDeTermos = 0

while termosParaMostrar > 0:
	while termo < primeiroTermo + termosParaMostrar * razao:
		print(termo, end=" -> ")
		termo += razao
		quantidadeDeTermos += 1
	print("PAUSA")

	termosParaMostrar = int(input("Quantos termos você quer mostrar a mais? "))
	primeiroTermo = termo
print("Progressão finalizada com {} termos mostrados.".format(quantidadeDeTermos))
