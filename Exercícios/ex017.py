"""
Exercício 17: Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

from math import pow, sqrt

oposto = float(input("Comprimento do cateto oposto (m): "))
adjacente = float(input("Comprimento do cateto adjacente (m): "))
hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2)) # math.hypot(oposto, adjacente)
print("A hipotenusa vale {:.2f}m".format(hipotenusa))
