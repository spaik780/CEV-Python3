var = input("Escreva algo: ")
# var = "Test"

print(var * 5)               # "TestTestTestTestTest"
print("{:^20}".format(var))  # "        Test        "
print("{:>20}".format(var))  # "                Test"
print("{:<20}".format(var))  # "Test                "
print("{:=^20}".format(var)) # "========Test========"

valor = float(input("Digite um valor: R$"))
# valor = 99.7

print("{:.0f}".format(valor)) # "100"
print("{:.2f}".format(valor)) # "99.70"
