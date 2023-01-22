"""
Exercício 60: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

print("{:-^40}".format(" CÁLCULO DE FATORIAL "))
numero = int(input("Digite um número: "))
contador = numero
fatorial = 1

print("{}! = ".format(numero), end="")
while contador > 0:
    print(contador, end=" x " if contador > 1 else " = ")
    fatorial *= contador
    contador -= 1
print(fatorial)
