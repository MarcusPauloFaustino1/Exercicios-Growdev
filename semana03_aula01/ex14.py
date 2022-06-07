'''Desenvolver um programa que efetue a soma de todos os números ímpares
que se encontram no conjunto dos números de 1 até 500.'''

print(f'\n{" SOMA DOS NÚMEROS ÍMPARE DE 1 ATÉ 500 ":=^60}\n') 

lista = []

n = 0

for i in range(500):
    n += 1
    if n % 2 != 0:
        lista.append(n)
total = sum(lista)    


print(f'A soma dos números ímpares de 1 até 500 é:\n\n {total:*^30}')

print(f'\n{"="*60}\n') 