"""
Exercício 44: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

precoDaCompra = float(input("Valor a ser pago: R$"))
print("-" * 35)
print("[1] À vista no dinheiro/cheque")
print("[2] À vista no cartão")
print("[3] Parcelado no cartão")
print("-" * 35)
formaDePagamento = int(input("Escolha uma forma de pagamento: "))

if formaDePagamento == 1:
	precoTotal = precoDaCompra - precoDaCompra * 0.1
elif formaDePagamento == 2:
	precoTotal = precoDaCompra - precoDaCompra * 0.05
elif formaDePagamento == 3:
	quantidadeDeParcelas = int(input("Em quantas vezes deseja pagar? "))
	if quantidadeDeParcelas <= 2:
		precoDaParcela = precoDaCompra / quantidadeDeParcelas
		precoTotal = precoDaCompra
		print("Sua compra será parcelada em {}x de R${:.2f} SEM JUROS.".format(quantidadeDeParcelas, precoDaParcela))
	else:
		precoDaParcela = (precoDaCompra + precoDaCompra * 0.2) / quantidadeDeParcelas
		precoTotal = quantidadeDeParcelas * precoDaParcela
		print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(quantidadeDeParcelas, precoDaParcela))
else:
	print("Opção Inválida.")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(precoDaCompra, precoTotal))
