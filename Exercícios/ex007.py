"""
Exercício 7: Média Aritmética
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota no aluno: "))
media = (nota1 + nota2) / 2
print("O aluno com as notas {:.1f} e {:.1f} tem como média {:.1f}.".format(nota1, nota2, media))
