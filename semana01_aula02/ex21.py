print("Entre com o valor aplicado mensalmente, o número de depósitos e a porcentagem (%) da rentabilidade mensal. ")

PMT = float(input("\nVocê vai aplicar quantos reais por mês?"))

n = int(input("\nVocê vai aplicar por quanto meses?:"))

ii = float(input("\nQual será a rentabilidade aplicada?"))

i = ii / 100

FV = (PMT*((((1 + i)**n) - 1)/i))

VTR = FV - n*PMT

print(f"\nO valor acumulado será de R$ {FV:.2f}   .")

print(f"\nO valor total do rendimento será igual a R$ {VTR:.2f}   .")
