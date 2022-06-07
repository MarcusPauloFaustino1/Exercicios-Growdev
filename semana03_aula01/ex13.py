'''Faça um programa que leia um valor N e mostre os N termos da Série a
seguir:
a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m'''

print(f'\n{" S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m ":=^60}\n') 

n = int(input('Insira o valor de N: '))

a = 1

ra = 1

m = 1

rm = 2

print(f'\n{"─"*60}\n')
print('Resultado:\n')
print(f'S = {a}/{m}',end="")

for i in range(n):
    a += ra
    m += rm
    print(f' + {a}/{m}', end="")

print(f'\n\n{"="*60}\n')    
print('\n\n')