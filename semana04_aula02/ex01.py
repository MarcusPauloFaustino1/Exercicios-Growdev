'''Faça um programa, com uma função que necessite de três argumentos, e
que forneça a soma desses três argumentos.'''

x = float(input('Digite um número: '))
y = float(input('Digite um número: '))
z = float(input('Digite um número: '))

def soma(x, y, z):
    s = x + y + z
    return s

print(f'{x} + {y} + {z} = {soma(x, y, z)}')