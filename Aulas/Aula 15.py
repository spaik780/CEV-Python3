soma = 0
contador = 0
while True:
	numero = int(input("Digite um número (999 para parar): "))
	if numero == 999:
		break
	soma += numero
	contador += 1
print(f"Você digitou {contador} números e a soma entre eles vale {soma}.")
