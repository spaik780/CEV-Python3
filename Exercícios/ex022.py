"""
Exercício 22: Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nomeCompleto = str(input("Digite seu nome completo: ")).strip()
nome = nomeCompleto.split()[0]

print("Seu nome em maiúsculas é {}.".format(nomeCompleto.upper()))
print("Seu nome em minúsculas é {}.".format(nomeCompleto.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nomeCompleto) - nomeCompleto.count(' ')))
print("Seu primeiro nome é {} e ele tem {} letras.".format(nome, len(nome)))
