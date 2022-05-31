paoFrances = 0.75

paoDoce = 0.85

quindim = 1.50

undPaoFrances = int(input("Quantas unidades de pão francês foram vendidas?"))

undPaoDoce = int(input("Quantas unidades de pão doce foram vendidas?"))

undQuindim = int(input("Quantas unidades de quindim foram vendidas?"))

paoFrances = float(input("Informe o preço do pão francês:"))

paoDoce = float(input("Informe o preço do pão doce:"))

quindim = float(input("Informe o preço do quindim:"))

total = paoFrances * undPaoFrances + paoDoce * undPaoDoce + quindim * undQuindim

imposto = total * 0.05

poupanca = total * 0.1

poupanca = (total - imposto)*0.1

print(f"\nO total faturado foi de R$ {total:.2f}")

print(f"\nVocê deverá pagar R$ {imposto:.2f} de impostos.")

print(f"\nR$ {poupanca:.2f} devem ser poupados.")