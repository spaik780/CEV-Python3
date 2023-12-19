"""
Exercício 115: Projeto
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from modulos.ex115.interface import *
from modulos.ex115.arquivo import *
from time import sleep

caminhoDoArquivo = "Exercícios/ex115_dados.txt"
if not arquivoExiste(caminhoDoArquivo):
	criarArquivo(caminhoDoArquivo)

while True:
	escolhaDoUsuario = menu("Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema")
	if escolhaDoUsuario == 1:
		cabecalho("PESSOAS CADASTRADAS")
		lerArquivo(caminhoDoArquivo)
	elif escolhaDoUsuario == 2:
		cabecalho("NOVO CADASTRO")
		nome = str(input("Nome: ")).strip().title()
		idade = leiaInt("Idade: ")
		gravar(caminhoDoArquivo, nome, idade)
	elif escolhaDoUsuario == 3:
		cabecalho("ATÉ LOGO!")	
		break
	else:
		print("\033[31mDigite uma opção válida.\033[m")
	sleep(1)
