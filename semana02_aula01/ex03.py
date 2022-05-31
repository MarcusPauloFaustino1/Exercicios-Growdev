'''Um brechó revende produtos usados, e fixa o preço de venda de cada
produto conforme o valor de sua aquisição. Se o preço de aquisição de um
produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45%
maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um
algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.'''



precoA = float(input("Digite o valor de aquisição do produto:"))

precoVm = precoA * 0.45 + precoA 

precoVM = precoA * 0.3 + precoA


if precoA < 50:
    precoV = precoVm
else:
    precoV = precoVM

print(f"O valor de venda do produto é:   {precoV:.2f}   .")
