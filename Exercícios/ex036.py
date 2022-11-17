"""
Exercício 36: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

valorDaCasa = float(input("Informe o valor do imóvel: R$"))
salarioDoComprador = float(input("Qual o salário do comprador? R$"))
anosParaPagar = int(input("Em quantos anos o comprador pretende pagar? "))
prestacaoMensal = valorDaCasa / (anosParaPagar * 12)
valorLimite = salarioDoComprador * 30 / 100

print("Para pagar uma casa de R${:.2f} em {} anos,".format(valorDaCasa, anosParaPagar), end=" ")
print("a prestação será de R${:.2f}.".format(prestacaoMensal))
if prestacaoMensal > valorLimite:
	print("Empréstimo NEGADO!")
else:
	print("Empréstimo ACEITO!")
