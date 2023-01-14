"""
Exercício 49: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""

numero = int(input("Digite um número para ver a sua tabuada: "))
print("\n{:=^20}".format(" Tabuada do {} ".format(numero)))

for fator in range(1, 11):
	print("{} x {:<2} = {}".format(numero, fator, numero * fator))
print("=" * 20)
