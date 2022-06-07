'''Escrever um programa que lê 5 valores para a, um de cada vez, e conta
quantos destes valores são negativos, escrevendo esta informação.'''

from time import sleep


print(f"\n{'QUANTOS SÃO NEGATIVOS?':=^40}\n")

negativos = 0

for var in range(5):
    a = int(input('Digite um valor:'))
    if a < 0:
        negativos += 1

print(f'\n{"_"*40}\n')

print('RESULTADO:\n')
sleep(2)

if negativos == 1:
    print('Dos valores digitados 1 é negativo.')
else:
    print(f'Dos valores digitados {negativos} são negativos.')

print(f'\n{"="*40}\n')


