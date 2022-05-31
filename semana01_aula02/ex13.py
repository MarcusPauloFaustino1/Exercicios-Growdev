from time import sleep


variavelA = input("Digite o valor da variável A:")

variavelB = input("Digite o valor da variável B:")

print("\nVariável A:", variavelA)
print("\nVariável B:", variavelB)

print("\nAgora vamos inverter...")

sleep(2)

aux = variavelB

variavelB = variavelA

variavelA = aux

print("\nVariável A:", variavelA)
print("\nVariável B:", variavelB)