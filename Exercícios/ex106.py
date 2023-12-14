"""
Exercício 106: Interactive Helping System
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
"""

from time import sleep

cores = {
	"NENHUMA": "\033[m",
	"VERDE": "\033[0;37;42m",
	"VERMELHO": "\033[0;37;41m",
	"AZUL": "\033[0;37;44m",
	"BRANCO": "\033[0;30;47m"
}


def aplicarCor(codigo=cores["NENHUMA"]):
	print(codigo, end="", flush=True)


def mostrarTitulo(texto, largura=0, altura=0):
	"""
	Mostra na tela determinado texto dentro de um bloco.
	Exemplo:
	╔════╗
	║ Oi ║
	╚════╝
	:param texto: Texto que será mostrado.
	:param largura: (Opcional) Espaçamento horizontal do texto.
	:param altura: (Opcional) Espaçamento vertical do texto.
	:return: Sem retorno.
	"""
	largura = len(texto) + largura * 2
	print("╔" + ("═" * largura) + "╗")
	print(("║" + (" " * largura) + "║\n") * altura, end="")
	print("║{:^{}}║".format(texto, largura))
	print(("║" + (" " * largura) + "║\n") * altura, end="")
	print("╚" + ("═" * largura) + "╝")


while True:
	aplicarCor(cores["VERDE"])
	mostrarTitulo("Interactive Helping System", 6, 1)
	aplicarCor()
	
	comando  = str(input("Função ou Biblioteca > "))
	if comando.upper() == "FIM": break

	aplicarCor(cores["AZUL"])
	mostrarTitulo(f"Acessando o manual do comando [{comando}]...", 4)
	sleep(1)
	aplicarCor()

	aplicarCor(cores["BRANCO"])
	help(comando)
	sleep(1)
	aplicarCor()
aplicarCor(cores["VERMELHO"])
mostrarTitulo("Até logo!", 2)
aplicarCor()
