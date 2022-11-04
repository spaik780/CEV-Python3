frase1 = "Fatiamento de String"
frase2 = "Linguagem Python"
frase3 = "   o rato roeu a roupa do rei de roma   "

print(frase1)         # "Fatiamento de String"
print(frase1[11])     # "d"
print(frase1[5:10])   # "mento"
print(frase1[0:10:2]) # "Ftaet"
print(frase1[:10])    # "Fatiamento"
print(frase1[14:])    # "String"
print(frase1[::2])    # "Ftaet eSrn"

print('=' * 20) # Separador

print(len(frase2))               # 16
print(frase2.count('n'))         # 2
print(frase2.count('n', 10, 16)) # 1
print(frase2.find("Python"))     # 10
print(frase2.find("Java"))       # -1
print("Python" in frase2)        # True

print('=' * 20) # Separador

print(frase2.replace("Python", "Java")) # "Linguagem Java"
print(frase2.lower())                   # "linguagem python"
print(frase2.upper())                   # "LINGUAGEM PYTHON"

print(frase3.strip())  # "o rato roeu a roupa do rei de roma"
print(frase3.rstrip()) # "   o rato roeu a roupa do rei de roma"
print(frase3.lstrip()) # "o rato roeu a roupa do rei de roma   "
frase3 = frase3.strip()

print(frase3.title())      # "O Rato Roeu A Roupa Do Rei De Roma"
print(frase3.capitalize()) # "O rato roeu a roupa do rei de roma"

print('=' * 20) # Separador

frase2Separada = frase2.split() # "Linguagem", "Python"
print(frase2Separada[1])        # "Python"
print('-'.join(frase2Separada)) # "Linguagem-Python"