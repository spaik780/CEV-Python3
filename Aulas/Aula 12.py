nome = str(input("Qual o seu nome? "))
if nome == "Igor":
	print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
	print("Seu nome é bem popular no Brasil.")
elif nome in "Sofia Emilly Jennifer":
	print("Belo nome feminino")
else:
	print("Seu nome é bem normal.")
print("Tenha um bom dia, {0}!".format(nome))
