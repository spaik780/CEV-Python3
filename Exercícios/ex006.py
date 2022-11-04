"""
Exercício 6: Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

numero = int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(numero, numero * 2))
print("O triplo de {} vale {}.".format(numero, numero * 3))
print("A raiz quadrada de {} vale {:.2f}.".format(numero, numero**0.5))
