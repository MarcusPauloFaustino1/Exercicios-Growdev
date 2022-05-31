print("Vamos calcular o volume de uma caixa? Para isso as medidas devem ser colocadas em metros!")

comprimento = float(input("Digite a medida do comprimento:"))

largura = float(input("Digite a medida da largura:"))

altura = float(input("Digite o valor da altura"))

volume = comprimento*largura*altura

print(f"O volume da sua caixa é de {volume:.2f}m³.")