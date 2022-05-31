n1 = float(input("Digite o valor a nota 1:"))

p1 = float(input("Digite o valor da porcentagem do peso da nota 1:"))

n2 = float(input("Digite o valor da nota 2:"))

p2 = float(input("Digite o valor da porcentagem do peso da nota 2:"))

n3 = float(input("Digite o valor da nota 3:"))

p3 = float(input("Digite o valor da porcentagem do peso da nota 3:"))

pp1 = p1 / 100

pp2 = p2 / 100

pp3 = p3 / 100

medPon = (n1*pp1 + n2*pp2 + n3*pp3)

print(f"\nSua média é {medPon:.1f}   .")
