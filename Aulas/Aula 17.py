numeros = [4, 5, 3, 1, 2]

numeros.sort(reverse=True) # [5, 4, 3, 2, 1]
numeros.sort() # [1, 2, 3, 4, 5]
numeros.append(6) # [1, 2, 3, 4, 5, 6]
numeros.insert(0, 0) # [0, 1, 2, 3, 4, 5, 6]

print(f"O número {numeros.pop()} foi removido da lista.")
print(numeros, end="\n\n") # [0, 1, 2, 3, 4, 5]

listaA = [2, 5, 3, 8]
listaB = listaA
listaB[2] = 4
print(f"Lista A: {listaA}") # [2, 5, 4, 8]
print(f"Lista B: {listaB}") # [2, 5, 4, 8]

listaC = [3, 2, 1, 4]
listaD = listaC[:]
listaD[2] = 2
print(f"Lista C: {listaC}") # [3, 2, 1, 4]
print(f"Lista D: {listaD}") # [3, 2, 2, 4]

comidasDoces = ["Cookie", "Bolo", "Pudim"]
comidasDoces.remove("Bolo") # ["Cookie", "Pudim"]

comidasSalgadas = ["Esfirra", "Pizza", "Burrito"]
del(comidasSalgadas[1]) # ["Esfirra", "Burrito"]
