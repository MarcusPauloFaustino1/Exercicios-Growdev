#Faça um algoritmo que receba um valor negativo e retorne o seu valor absoluto (ex: recebe -5 e retorna 5).

n = float(input("Digite um número negativo:"))

if n >= 0:
    print("Número inválido! Digite um número negativo.")
    n = float(input("Digite um número negativo:"))

nAbsoluto = n * -1

print(f" O valor absoluto de {n} é {nAbsoluto}   .")
