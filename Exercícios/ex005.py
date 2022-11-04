"""
Exercício 5: Antecessor e Sucessor
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = int(input("Digite um número: "))
sucessor = numero + 1
antecessor = numero - 1
print("Analisando o valor {}, seu sucessor é {} e seu antecessor é {}.".format(numero, sucessor, antecessor))
