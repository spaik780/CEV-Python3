"""
Exercício 27: Primeiro e último nome de uma pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nomeCompleto = str(input("Digite seu nome completo: ")).strip().split()
print("Primeiro Nome:", nomeCompleto[0])
print("Último Nome:", nomeCompleto[-1])
