"""
Exercício 26: Primeira e útima ocorrência de uma string
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra “A”.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
"""

frase = input("Digite alguma frase: ").strip().upper()
print("A letra \"A\" aparece {} vezes.".format(frase.count("A")))
print("A letra \"A\" aparece na posição {} pela primeira vez.".format(frase.find("A") + 1))
print("A letra \"A\" aparece na posição {} pela última vez.".format(frase.rfind("A") + 1))
