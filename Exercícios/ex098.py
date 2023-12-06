"""
Exercício 98: Função de Contador
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
- De 1 até 10, de 1 em 1
- De 10 até 0, de 2 em 2
- Uma contagem personalizada
"""

from time import sleep

def contador(inicio, fim, passo):
	if passo == 0:
		passo = 1
	elif passo < 0:
		passo *= -1
	print("-" * 50)
	print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
	if fim < inicio:
		fim -= 1
		if passo > 0:
			passo *= -1
	else:
		fim += 1
	sleep(1)
	for indice in range(inicio, fim, passo):
		print(indice, end=" ", flush=True)
		sleep(0.5)
	print(f"FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("-" * 50)
print("Agora é sua vez de personalizar a contagem!")
contador(
	inicio = int(input("Início: ")),
	fim = int(input("Fim: ")),
	passo = int(input("Passo: "))
)
