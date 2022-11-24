"""
Exercício 42: Analisando Triângulos v2.0
Refaça o Exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

primeiroSegmento = float(input("Primeiro Segmento: "))
segundoSegmento = float(input("Segundo Segmento: "))
terceiroSegmento = float(input("Terceiro Segmento: "))
maiorSegmento = max(primeiroSegmento, segundoSegmento, terceiroSegmento)
somaDosMenoresSegmentos = sum([primeiroSegmento, segundoSegmento, terceiroSegmento]) - maiorSegmento
if somaDosMenoresSegmentos > maiorSegmento:
	print("Os segmentos {},{},{} formam um triângulo".format(primeiroSegmento, segundoSegmento,terceiroSegmento), end=" ")
	if somaDosMenoresSegmentos == 2 * maiorSegmento:
		print("EQUILÁTERO")
	#TODO: Fazer o resto dos 2 triângulos
else:
	print("Os segmentos {},{},{} não podem formar um triângulo.".format(primeiroSegmento, segundoSegmento,terceiroSegmento))
