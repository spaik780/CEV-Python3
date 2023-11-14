"""
Exercício 72: Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numerosPorExtenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis","Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
	numero = int(input("Digite um número entre 0 e 20: "))
	if 0 <= numero <= 20: break
print(f"Você digitou o número {numerosPorExtenso[numero]}.")
