"""
Exercício 25: Procurando uma string dentro de outra
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = str(input("Digite um nome: ")).strip()
print("SILVA" in nome.upper())
