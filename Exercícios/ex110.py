"""
Exercício 110: Reduzindo o Programa
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from modulos.ex110 import moeda

preco = float(input("Digite o preço: R$"))
moeda.resumo(preco, 80, 35)
