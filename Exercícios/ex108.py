"""
Exercício 108: Formatando Moedas em Python
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
"""

from modulos.ex108 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}")
print(f"Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}")
