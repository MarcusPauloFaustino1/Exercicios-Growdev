from time import sleep


n1 = float(input("Digite um número:"))

n2 = float(input("Digite outro número:"))

adicao = n1 + n2

subtracao = n1 - n2

divisao = n1 / n2

multiplicacao = n1 *n2

print("Calculando...")

sleep(2)

print(f"\n{n1} + {n2} = {adicao} ")

print(f"\n{n1} - {n2} = {subtracao}")

print(f"\n{n1} / {n2} = {divisao}")

print(f"\n{n1} x {n2} = {multiplicacao}")

