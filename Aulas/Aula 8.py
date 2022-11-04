from math import floor, sqrt
import random
# sqrt: Raíz quadrada
# floor: Arredondamento para baixo

numero = int(input("Digite um número: "))
raiz = sqrt(numero)
print("A raíz de {} é igual a {}".format(numero, floor(raiz)))

numeroAleatorio = random.randint(1, 10) # Número aleatório (1, 2, 3, ..., 10)
print("Número aleatório: {}".format(numeroAleatorio))
