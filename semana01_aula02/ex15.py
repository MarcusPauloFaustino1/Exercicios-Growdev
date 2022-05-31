v1 = float(input("Digite o valor do produto 1:"))
v2 = float(input("Digite o valor do produto 2:"))
v3 = float(input("Digite o valor do produto 3:"))
v4 = float(input("Digite o valor do produto 4:"))
v5 = float(input("Digite o valor do produto 5:"))

subTotal = v1 + v2 + v3 + v4 + v5

imposto = subTotal * 0.06

total = subTotal + imposto

print(f"\nSubtotal da venda: R$ {subTotal}\n\nValor do imposto: R$ {imposto:.2f}\n\nValor total: R${total:.2f}.")
