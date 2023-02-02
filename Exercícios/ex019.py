"""
Exercício 19: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = choice(listaDeAlunos)
print("O aluno escolhido foi {}".format(alunoEscolhido))
