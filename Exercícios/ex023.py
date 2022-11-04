"""
Exercício 23: Separando dígitos de um número
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

numero = "0000" + str(input("Digite um número de 0 a 9999: "))
print("Unidade:", numero[-1])
print("Dezena:", numero[-2])
print("Centena:", numero[-3])
print("Milhar:", numero[-4])
