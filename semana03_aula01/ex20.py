'''Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.G. contendo 10 valores.'''

print(f'\n{" PROGRASSÃO  GEOMÉTRICA ":=^60}\n')

a = int(input('Insira o valor inicial da PG: '))

r = int(input('Insira a razão: '))

pg = []

for i in range(10):
    pg.append(a)
    a = a * r

print(f'\n{"─"*60}\n')
print(f'Sequência em P.G.: {pg}')
print(f'\n{"="*60}\n')