"""
Exercício 40: Aquele Clássico da Média
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, conforme a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

primeiraNota = float(input("Primeira nota: "))
segundaNota = float(input("Segunda nota: "))
media = (primeiraNota + segundaNota) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é de {:.1f}".format(primeiraNota, segundaNota, media))
if media < 5.0:
	print("O aluno foi REPROVADO.")
elif media < 7.0:
	print("O aluno está de RECUPERAÇÃO.")
elif media >= 7.0:
	print("O aluno foi APROVADO.")
