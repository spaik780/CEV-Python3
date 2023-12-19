try:
	numerador = int(input("Numerador: "))
	denominador = int(input("Denominador: "))
	divisao = numerador / denominador
except (ValueError, TypeError):
	print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
	print("Não é possível dividir um número por zero!")
except Exception as erro:
	print("O erro encontrado foi", erro.__cause__)
else:
	print(f"O resultado da divisão é {divisao:.1f}!")
finally:
	print("Volte sempre!")
