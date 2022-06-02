'''Escrever um programa que lê um valor N inteiro e positivo e que calcula e
escreve o valor de E.
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!'''

from time import sleep

print(f'\n{"CALCULANDO FÓRMULA":=^60}\n')

print("E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N! +1\n")

n = int(input('Digite um valor inteiro e positivo para N: '))

print('Calculando...')
sleep(2)

fatorial = 1
lista = []
lista2 = []
nfatorial = 1


lista.append(1)

for num in range(1, n):
    fatorial *= num + 1
    fatorial2 = fatorial + 1
    lista.append(fatorial2)
   

for num in range(1, n):
    nfatorial *= num + 1
    nfatorial2 = nfatorial + 1
    lista2.append(nfatorial2)

for i in range(1, len(lista2)):
    x = lista[0]/lista2[0]
    
    for i in range(1, len(lista2)):
        x = x / lista2[i]

print('\nE = 1 + 1 / ',end="")
for i in range(1, n):
    e = 1 + i
    print(f'{i}! + 1 / ', end="")
    
print(f'{n}! +1')        

  
print(f'\n{"_"*60}\n')
print(f'E = {x:.10f}')  
print(f'\n{"="*60}\n', end="")
    
