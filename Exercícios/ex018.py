"""
Exercício 18: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians

angulo = float(input("Digite um ângulo qualquer: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("Seno de {}°: {:.2f}".format(angulo, seno))
print("Cosseno de {}°: {:.2f}".format(angulo, cosseno))
print("Tangente de {}°: {:.2f}".format(angulo, tangente))
