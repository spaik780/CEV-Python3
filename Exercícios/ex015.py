"""
Exercício 15: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

km = float(input("Digite a quantidade de KM percorridos: "))
dia = int(input("Quantidade de dias que ele foi alugado: "))
valor = (0.15 * km) + (60 * dia)
print("Total a ser pago: R${:.2f}.".format(valor))
