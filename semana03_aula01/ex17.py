'''Crie um programa para que retorne o somatório de todos os números entre 1
e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o
número 4, o computador deverá calcular o somatório 1 + 2 + 3 + 4 = 10.'''

print(f'\n{" SOMATÓRIO DOS NÚMEROS ENTRE 1 -> N ":=^60}\n') 

n = int(input('Forneça um valor para N: '))

soma = 0

for i in range(1, n+1):
    soma += 1 * i

print(f'\nResultado:\n\n {soma}')
print(f'\n{"="*60}\n') 