"""
Exercício 11: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
print("A quantidade de tinta necessária para pintar uma parede de {}m² é {}L.".format(area, area / 2))
