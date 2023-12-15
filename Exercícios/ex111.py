"""
Exercício 111: Transformando Módulos em Pacotes
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

from modulos.ex111.utilidadesCeV import moeda

preco = float(input("Digite o preço: R$"))
moeda.resumo(preco, 35, 22)
