'''19) Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo. Exemplos:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades'''

from time import sleep

print(f'{"CENTENAS DEZENAS UNIDADES":=^50}')

n = int(input('\nDigite um número inteiro menor que 1000:'))

centenas = n // 100
rcentenas = n % 100

dezenas = (rcentenas * 100) // 1000

unidades = n % 10

print('Separando Centenas, Dezenas e Unidades...')
sleep(2)

print(f"{'_':_^50}")
print(f'\nCentenas: {centenas}\nDezenas:  {dezenas}\nUnidades: {unidades}')
print(f"\n{'=':=^50}")