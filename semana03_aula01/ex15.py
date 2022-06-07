'''Escreva um programa que imprima na tela para escrever a tabuada de um
número fornecido pelo usuário, de 1 a 10.'''

print(f'\n{" TABUADA ":=^60}\n') 

n = float(input('Digite um número: '))

print(f'+{"─"*15}+')

for i in range(1,10):
    if n * i < 10:
        print(f'{n} X {i} = {n * i}')
    elif n* i < 100:
        print(f'{n} X {i} = {n * i}')
    else:
        print(f'{n} X {i} = {n * i}')

print(f'+{"─"*15}+')
print(f'\n{"="*60}\n') 