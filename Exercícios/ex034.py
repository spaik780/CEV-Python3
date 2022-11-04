"""
Exercício 34: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input("Informe o salário do funcionário: R$"))
if salario > 1250:
	novoSalario = salario + salario * 0.10
else:
	novoSalario = salario + salario * 0.15
print("O novo salário será de R${:.2f}.".format(novoSalario))
