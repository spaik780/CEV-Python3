"""
Exercício 29: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

velocidade = float(input("Informe a velocidade do carro (km/h): "))
if velocidade > 80:
	total = (velocidade - 80) * 7
	print("Você excedeu o limite de velocidade!")
	print("Multa: R${:.2f}".format(total))
print("Tenha um boa dia! Dirija com segurança!")
