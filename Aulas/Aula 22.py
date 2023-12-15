import uteis
from uteis import numeros, datas

uteis.mostrarLinha(50)
numero = int(input("Digite um valor: "))

fatorial = numeros.calcularFatorial(numero)
dobro = numeros.calcularDobro(numero)
triplo = numeros.calcularTriplo(numero)

print(f"O fatorial de {numero} é {fatorial}")
print(f"O dobro de {numero} é {dobro}")
print(f"O triplo de {numero} é {triplo}")

uteis.mostrarLinha(50)
anoDeNascimento = int(input("Informe seu ano de nascimento: "))
print(f"Sua idade é {datas.calcularIdade(anoDeNascimento)}.")

uteis.mostrarLinha(50)
