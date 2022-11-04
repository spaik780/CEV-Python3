"""
Exercício 13: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input("Informe o salário do funcionário: R$"))
print("O salário agora é de R${:.2f}".format(salario * 1.15))
