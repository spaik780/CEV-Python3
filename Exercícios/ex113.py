"""
Exercício 113: Funções Aprofundadas em Python
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

from modulos.ex113.ValidadorDeDados import leiaInt, leiaFloat

numeroInteiro = leiaInt("Digite um número inteiro: ")
numeroReal = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {numeroInteiro} e o real foi {numeroReal}.")
