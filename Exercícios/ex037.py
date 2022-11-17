"""
Exercício 37: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

numeroDecimal = int(input("Digite um número inteiro qualquer: "))
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")
baseDeConversao = str(input("Qual será a base de conversão? ")).lower()
if baseDeConversao in ["1", "binário"]:
	print("{:b}".format(numeroDecimal))
elif baseDeConversao in ["2", "octal"]:
	print("{:o}".format(numeroDecimal))
elif baseDeConversao in ["3", "hexadecimal"]:
	print("{:x}".format(numeroDecimal))
else:
	print("Opção Inválida!")
