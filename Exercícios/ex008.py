"""
Exercício 8: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input("Digite uma medida em metros: "))
print("{}m equivalem a {}km".format(medida, medida / 1000))
print("{}m equivalem a {}hm".format(medida, medida / 100))
print("{}m equivalem a {}dam".format(medida, medida / 10))
print("{}m equivalem a {}dm".format(medida, medida * 10))
print("{}m equivalem a {}cm".format(medida, medida * 100))
print("{}m equivalem a {}mm".format(medida, medida * 1000))
