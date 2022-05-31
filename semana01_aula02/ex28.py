num = float(input("Digite um número:"))
numInt = int(num)

pontFloat = num - numInt

num2 = float(input("Digite outro número:"))
numInt2 = int(num2)

pontFloat2 = num2 - numInt2

num3 = float(input("Digite mais um número:"))
numInt3 = int(num3)

pontFloat3 = num3 - numInt3

soma = pontFloat + pontFloat2 + pontFloat3

print(f"A soma das partes decimais desses números é igual a {soma:.6f}    .")