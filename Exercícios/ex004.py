"""
Exercício 4: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

var = input("var = ")
print("type(var) : ", type(var))
print("var.isalnum() :", var.isalnum())
print("var.isalpha() :", var.isalpha())
print("var.isascii() :", var.isascii())
print("var.isdecimal() :", var.isdecimal())
print("var.islower() :", var.islower())
print("var.isupper() :", var.isupper())
print("var.isspace() :", var.isspace())
print("var.isnumeric() :", var.isnumeric())
print("var.istitle() :", var.istitle())
print("var.isprintable() :", var.isprintable())
print("var.isdigit() :", var.isdigit())
print("var.isnumeric() :", var.isnumeric())
