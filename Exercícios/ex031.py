"""
Exercício 31: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input("Informe a distância da sua viagem (Km): "))
if distancia <= 200:
	passagem = distancia * 0.50
else: 
	passagem = distancia * 0.45
print("o custo da Passagem será de R${:.2f}.".format(passagem))
