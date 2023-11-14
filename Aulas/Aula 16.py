lanche = ("Hambúrger", "Suco", "Pizza", "Pudim")

print(lanche[1]) # Suco
print(lanche[-1]) # Pudim
print(lanche[1:3]) # ('Suco', 'Pizza')

print(len(lanche)) # 4

print(sorted(lanche)) # Ordem Alfabética

for comida in lanche:
	print(comida)  

for c in range(0, len(lanche)):
	print(f"{lanche[c]} na posição {c}")

for pos, comida in enumerate(lanche):
	print(f"{comida} na posição {pos}")

tuplaA = (1, 2, 3)
tuplaB = (3, 4, 5)
tuplaC = tuplaA + tuplaB # (1, 2, 3, 3, 4, 5)

print(tuplaC.count(3)) # 2
print(tuplaC.index(3)) # 2
print(tuplaC.index(3, 3)) # 3

del(lanche, tuplaA, tuplaB, tuplaC)
