'''O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
escrever o custo final ao consumidor.'''

from time import sleep


print(f"\n{'CUSTO FINAL AO CONSUMIDOR':=^70}\n")

custoFabrica = float(input("Digite o custo de fábrica:"))

print('Calculando...')
sleep(2)

percentDistribuidor = custoFabrica * 0.28

impostos = custoFabrica * 0.45

custoConsumidor = custoFabrica + percentDistribuidor + impostos

print(f"\n{'_':_^70}\n")

print(f"\n\nCusto do carro ao consumidor: R$ {custoConsumidor:.2f}\n\nSendo...\n\nPercentual do distribuidor:   R$ {percentDistribuidor:.2f}\n\nImpostos:                     R$ {impostos}\n\nCusto de fábrica:             R$ {custoFabrica}\n\n ")

print(f"\n{'=':=^70}\n")
