'''Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um
produto.
a) Calcular e escrever o total

total = quantidade adquirida * preço unitário
b) Leia o desconto sobre a compra e calcule.

total a pagar = total - desconto
i) Sabendo-se que:
(1) Se quantidade <= 5 o desconto será de 2%.
(2) Se quantidade > 5 e quantidade <=10 o desconto será de
3%.
(3) Se quantidade > 10 o desconto será de 5%.'''

print(f"\n{'PRODUTOS E PREÇOS':=^70}\n")

pUnitario = float(input("Digite o preço unitário do produto:"))

quantAdquirida = int(input("\nDigite a quantidade adquirida:"))

if quantAdquirida < 1:
    print("Quantidade inválida!")
    quantAdquirida = int(input("Digite a quantidade adquirida:"))

print(f"\n{'_':_^70}\n")

total = pUnitario * quantAdquirida

desc1 = total * 0.02

desc2 = total * 0.03

desc3 = total * 0.05

totalPagar1 = total - desc1

totalPagar2 = total - desc2

totalPagar3 = total - desc3

if quantAdquirida <= 5:
    print(f"Total a pagar:          R$ {totalPagar1:.2f}")
    print(f"\nVocê recebeu um desconto de R$ {desc1:.2f}")
    print(f"\n{'=':=^70}\n")
elif quantAdquirida > 5 and quantAdquirida <= 10:
    print(f"Total a pagar:          R$ {totalPagar2:.2f}")
    print(f"\nVocê recebeu um desconto de R$ {desc2:.2f}")
    print(f"\n{'=':=^70}\n")
else:
    print(f"Total a pagar:          R$ {totalPagar3:.2f}")
    print(f"\nVocê recebeu um desconto de R$ {desc3:.2f}")
    print(f"\n{'=':=^70}\n")
