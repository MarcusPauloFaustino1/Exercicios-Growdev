'''Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.A. contendo 10 valores.'''

print(f'\n{" PROGRASSÃO ARITMÉTICA ":=^60}\n')
a = int(input('Insira o valor inicial da P.A.: '))

r = int(input('Insira a razão: '))

pa = []

for i in range(10):
    pa.append(a)
    a = a + r

print(f'\n{"─"*60}\n')
print(f'Sequência em P.A.: {pa}')
print(f'\n{"="*60}\n')

