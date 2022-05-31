valor = float(input("Digite uma quantia de dinheiro:"))
intValor = int(valor)

resto1 = valor - intValor

resto2 = resto1 - 0.5

resto3 = resto2 - 0.25

resto4 = resto3 - 0.1

resto5 = resto3 - 0.05


print(f"Quantidades de moedas de R$ 1: {intValor}")

if resto1 >= 0.5:
    print("Quantidade de moedas de R$ 0,50: 1")

elif resto1 < 0.5:
    print("Quantidade de moedas de R$ 0,50: 0")

if resto2 <= 0.251:
    print("Quantidade de moedas de R$ 0,25: 1")

elif resto2 <= 0.241:
    print("Quantidade de moedas de R$ 0,25: 0")

if resto3  <= 0.241 and resto3 > 0.191:
    print("Quantidade de moedas de R$ 0,10: 2")

elif resto3 <= 0.191 and resto3 > 0.091:
    print("Quantidade de moedas de R$ 0,10: 1")

elif resto3 <= 0.091:
    print("Quantidade de moedas de R$ 0,10: 0")

if resto4 <= 0.091 and resto4 > 0.041:
    print("Quantidade de moedas de R$ 0,5: 1")
elif resto4 <= 0.041:
    print("Quantidade de moedas de R$ 0,5: 1")

if resto5 >= 0.04 and resto5 < 0.041:
    print("Quantidade de moedas de R$ 0,01: 4")
elif resto5 >= 0.03 and resto5 < 0.031:
    print("Quantidade de moedas de R$ 0,01: 3")
elif resto5 >= 0.02 and resto5 < 0.021:
    print("Quantidade de moedas de R$ 0,01: 2")
elif resto5 >= 0.01 and resto5 < 0.011:
    print("Quantidade de moedas de R$ 0,01: 1")
elif resto5 >= 0.00 and resto5 < 0.001:
    print("Quantidade de moedas de R$ 0,01: 0")


if resto1 < 0.50 and resto1 > 0.24:
    print("Quantidade de moedas de R$ 0,25: 1")
elif resto1 < 0.25:
    print("Quantidade de moedas de R$ 0,25: 0")

if resto1 < 0.25 and resto1 > 0.19:
    print("Quantidade de moedas de R$ 0,10: 2")
elif resto1 < 0.2 and resto1 > 0.9:
    print("Quantidade de moedas de R$ 0,10: 1")
elif resto1 < 0.1:
    print("Quantidade de moedas de R$ 0,10: 0")

if resto1 < 0.1 and resto1 > 0.041:
    print("Quantidade de moedas de R$ 0,05: 1")
elif resto1 < 0.05:
    print("Quantidade de moedas de R$ 0,05: 0")
    
if resto1 >= 0.04 and resto1 < 0.041:
    print("Quantidade de moedas de R$ 0,01: 4")
elif resto1 >= 0.03 and resto1 < 0.031:
    print("Quantidade de moedas de R$ 0,01: 3")
elif resto1 >= 0.02 and resto1 < 0.021:
    print("Quantidade de moedas de R$ 0,01: 2")
elif resto1 >= 0.01 and resto1 < 0.011:
    print("Quantidade de moedas de R$ 0,01: 1")
elif resto1 >= 0.00 and resto1 < 0.001:
    print("Quantidade de moedas de R$ 0,01: 0")



