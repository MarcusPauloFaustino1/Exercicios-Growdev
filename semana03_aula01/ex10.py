'''Escreva um programa que recebe 10 valores e imprima o somatório dos
elementos.'''

print(f'\n{" SOMA DE VALORES":=^60}\n')

lista = []

for i in range(10):
    val = float(input('Digite um valor: '))
    lista.append(val)

total = sum(lista)

print(f'\n{"─"*60}\n')
print(f'Somatório: {total}')
print(f'\n{"="*60}\n')