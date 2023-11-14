"""
Exercício 73: Tuplas com Times de Futebol
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
- Os 5 primeiros.
- Os últimos 4 colocados.
- Times em ordem alfabética.
- Em que posição está o time da Chapecoense.
"""

times = ("Flamengo", "Cruzeiro", "Grêmio", "São Paulo", "Internacional", "Sport Recife", "Palmeiras", "Corinthians", "Fluminense", "Atlético", "América-MG", "Botafogo", "Vasco da Gama", "Chapecoense", "Santos", "Atlético-PR", "EC Vitória", "Bahia", "Paraná", "Ceará SC")

print("Lista de times do Brasileirão:", times)
print("Os cinco primeiros são: ", times[:5])
print("Os quatro últimos são: ", times[-4:])
print("Times em ordem alfabética: ", sorted(times))
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")
