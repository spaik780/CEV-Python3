"""
\033[<estilo>;<texto>;<fundo>m

Exemplos:
\033[0;30;41m -> Sem Estilo, Texto Branco, Fundo Vermelho
\033[4;33;44m -> Sublinhado, Texto Amarelo, Fundo Azul
\033[1;35;43m -> Negrito, Texto Roxo, Fundo Amarelo
\033[30;42m   -> Sem Estilo, Texto Branco, Fundo Verde
\033[m        -> Sem Estilo, Texto Padrão, Fundo Padrão
\033[7;30m    -> Negativo, Letra Preta, Fundo Branco

Estilo
0 -> Sem Estilo
1 -> Negrito
4 -> Sublinhado
7 -> Negativo

Texto
30 -> Branco
31 -> Vermelho
32 -> Verde
33 -> Amarelo
34 -> Azul
35 -> Roxo
36 -> Ciano
37 -> Cinza

Fundo
40 -> Branco
41 -> Vermelho
42 -> Verde
43 -> Amarelo
44 -> Azul
45 -> Roxo
46 -> Ciano
47 -> Cinza
"""

numero1 = 6
numero2 = 4
soma = numero1 + numero2
print("\033[36m{} \033[m+ \033[36m{} \033[m= \033[33m{}\033[m".format(numero1, numero2, soma))
