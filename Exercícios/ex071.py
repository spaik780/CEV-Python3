"""
Exercício 71: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""

valorDoSaque = 0

print("=" * 40)
print("{:^40}".format("BANCO CEV"))
print("=" * 40)

valorDoSaque = float(input("Que valor você quer sacar? R$"))
for valorDaCedula in [50, 20, 10, 1]:
	quantidadeDeCedulas = int(valorDoSaque // valorDaCedula)
	if quantidadeDeCedulas > 0:
		print(f"Total de {quantidadeDeCedulas} cédula{'s' if quantidadeDeCedulas > 1 else ''} de R${valorDaCedula}")
		valorDoSaque -= valorDaCedula * quantidadeDeCedulas
print("=" * 40)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
