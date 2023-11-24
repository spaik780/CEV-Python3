"""
Exercício 81: Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
- Quantos números foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []
while True:
	valores.append(int(input("Digite um valor: ")))
	querContinuar = str(input("Deseja continuar? [S/N] "))[0].upper()
	if querContinuar == "N": break
valores.sort(reverse=True)
print("-" * 50)
print(f"Você digitou {len(valores)} elementos.")
print(f"Os valores em ordem decrescente são {valores}")
print(f"O valor 5 {'faz' if 5 in valores else 'não faz'} parte da lista.")
