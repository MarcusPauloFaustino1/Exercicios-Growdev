'''Desenvolver um programa que leia um número não determinado de valores
e calcule e escreva a média aritmética dos valores lidos, a quantidade de
valores positivos, a quantidade de valores negativos e o percentual de
valores negativos e positivos.'''


from statistics import mean

print(f'\n{" MÉDIAS, POSITIVOS E NEGATIVOS ":=^60}\n')

lista = []

positivos = 0

negativos = 0

valorDigitado = 's'

while valorDigitado == 's':
    valor = float(input('Digite um valor: '))
    lista.append(valor)
    media = mean(lista)
    if valor < 0:
        negativos += 1
    elif valor >= 0:
        positivos += 1
    valorDigitado = input('Deseja inserir mais números [s / n]: ')

else: 
    pass

percentPositivos = (100 * positivos)/len(lista)
percentNegativos = (100 * negativos)/len(lista)

print(f'\n{"─"*60}\n')

print(f'\nMédia Aritmética dos Valores digitados: {media:.2f}\n')
print(f'Quantidades de Valores Positivos: {positivos}\n')
print(f'Quantidades de Valores Negativos: {negativos}\n')
print(f'Percentual de Valores Positivos: {percentPositivos:.2f}\n')
print(f'Percentual de Valores Negativos: {percentNegativos:.2f}\n')

print(f'\n{"="*60}\n')



