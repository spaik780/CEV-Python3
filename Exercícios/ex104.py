"""
Exercício 104: Validando Entrada de Dados
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: numero = leiaInt("Digite um número: ")
"""

def leiaInt(prompt):
	while True:
		numero = str(input(prompt)).strip()
		if numero.isnumeric():
			break
		else:
			print(f"ERRO: Número Inválido!")
	return int(numero)


numero = leiaInt("Digite um número: ")
print(f"Você digitou o número {numero}.")
