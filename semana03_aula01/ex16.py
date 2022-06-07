'''Escreva um programa que conte em ordem reversa, de 25 a zero.'''

from time import sleep

print(f'\n{" TIMER 25 -> 0 ":=^30}\n') 

print('Contagem Regressiva:\n')
n = 25

for i in range(26):
    sleep(0.5)
    print(n)
    n -= 1

print('\nPrograma Finalizado')
print(f'\n{"="*30}\n')
