print("ax² + bx +c")

a = float(input("\nDigite o valor do coeficiente a:"))

b = float(input("Digite o valor do coeficiente b:"))

c = float(input("Digite o valor do coeficiente c:"))

x1 = ((-1*b) + ((b**2 - 4*a*c)**0.5))/2*a

x2 = ((-1*b) - ((b**2 - 4*a*c)**0.5))/2*a

print(f"\nx1 = {x1:.2f}")

print(f"\nx2 = {x2:.2f}")
