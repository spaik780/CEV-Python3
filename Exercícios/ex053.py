"""
Exercício 53: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = str(input("Digite um frase: ")).replace(" ", "").upper()
fraseInversa = frase[::-1]
print("O inverso de {} é {}".format(frase, fraseInversa))
print("A frase digitada {} um palíndromo!".format("não é" if frase != fraseInversa else "é"))
