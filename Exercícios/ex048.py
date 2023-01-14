"""
Exercício 48: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

somatoriaDosNumeros = 0
quantidadeDeNumeros = 0
for n in range(1, 501, 2):
	if n % 3 == 0:
		quantidadeDeNumeros += 1
		somatoriaDosNumeros += n
print("A soma de todos os {} valores solicitados é {}".format(quantidadeDeNumeros, somatoriaDosNumeros))
