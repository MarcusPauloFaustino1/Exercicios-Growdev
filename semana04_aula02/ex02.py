'''Faça um programa, com uma função que necessite de um argumento. A
função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
se seu argumento for zero ou negativo.'''

x = float(input('Digite um número: '))

def pn(x):
    if x > 0:
        return 'P'
    elif x <= 0:
        return 'N'

print(pn(x))